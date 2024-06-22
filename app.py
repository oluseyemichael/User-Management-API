from flask import Flask, request, jsonify, abort
from models import db, UsersDatabase

app = Flask(__name__)

# Configuration for SQLAlchemy database URI and disabling modification tracking
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create database tables before the first request is handled
with app.app_context():
    db.create_all()

# Route to create a new user
@app.route('/data/create', methods=['POST'])
def create():
    data = request.get_json()  # Get JSON data from the request
    if not data:
        abort(400, description="No input data provided")  # Return 400 if no data is provided
    # Extract fields from JSON data
    username = data.get('username')
    fullname = data.get('fullname')
    age = data.get('age')
    gender = data.get('gender')
    email = data.get('email')
    if not username or not fullname or not age or not gender or not email:
        abort(400, description="Missing fields")  # Return 400 if any required field is missing
    # Create a new user instance
    user = UsersDatabase(username=username, fullname=fullname, age=age, gender=gender, email=email)
    db.session.add(user)  # Add user to the session
    db.session.commit()  # Commit the session to save the user
    return jsonify({'message': 'User created successfully'}), 201  # Return success message

# Route to retrieve all users
@app.route('/data', methods=['GET'])
def RetrieveList():
    users = UsersDatabase.query.all()  # Query all users from the database
    return jsonify([user.to_dict() for user in users]), 200  # Return list of users in JSON format

# Route to retrieve a specific user by ID
@app.route('/data/<int:id>', methods=['GET'])
def RetrieveUser(id):
    user = UsersDatabase.query.filter_by(id=id).first()  # Query user by ID
    if user:
        return jsonify(user.to_dict()), 200  # Return user data if found
    return jsonify({'message': f"User with id = {id} does not exist"}), 404  # Return 404 if user not found

# Route to update a user by ID
@app.route('/data/<int:id>/update', methods=['PUT'])
def update(id):
    data = request.get_json()  # Get JSON data from the request
    if not data:
        abort(400, description="No input data provided")  # Return 400 if no data is provided
    user = UsersDatabase.query.filter_by(id=id).first()  # Query user by ID
    if user:
        # Extract fields from JSON data
        username = data.get('username')
        fullname = data.get('fullname')
        age = data.get('age')
        gender = data.get('gender')
        email = data.get('email')
        if not username or not fullname or not age or not gender or not email:
            abort(400, description="Missing fields")  # Return 400 if any required field is missing
        # Update user fields
        user.username = username
        user.fullname = fullname
        user.age = age
        user.gender = gender
        user.email = email
        db.session.commit()  # Commit the session to save changes
        return jsonify({'message': 'User updated successfully'}), 200  # Return success message
    return jsonify({'message': f"User with id = {id} does not exist"}), 404  # Return 404 if user not found

# Route to delete a user by ID
@app.route('/data/<int:id>/delete', methods=['DELETE'])
def delete(id):
    user = UsersDatabase.query.filter_by(id=id).first()  # Query user by ID
    if user:
        db.session.delete(user)  # Delete user from the session
        db.session.commit()  # Commit the session to delete the user
        return jsonify({'message': 'User deleted successfully'}), 204  # Return success message
    return jsonify({'message': f"User with id = {id} does not exist"}), 404  # Return 404 if user not found

# Run the Flask app
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
