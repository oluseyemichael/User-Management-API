# User Management API

## Overview
This project is a simple user management system implemented as a backend API using Flask. The API allows for the creation, retrieval, updating, and deletion of users. Users can be managed by their unique ID or username.

## Features
- **Create a New User:** Users can be created by sending a POST request with the user’s details in the request body.
- **Retrieve User Information:**
  - By ID: Sending a GET request to a specific URL endpoint with the user's ID.
  - By Name: Sending a GET request with the user's name as a query parameter.
- **Update User Information:**
  - By ID: Sending a PUT request with the user’s new details in the request body and the user’s ID in the URL.
  - By Name: Sending a PUT request with the user’s new details in the request body and the old name as a query parameter.
- **Delete a User:**
  - By ID: Sending a DELETE request to a specific URL endpoint with the user’s ID.
  - By Name: Sending a DELETE request with the user’s name as a query parameter.

## Technical Specifications
- **API Framework:** Flask
- **Data Persistence:** SQLite using SQLAlchemy
- **Error Handling:** Proper error handling to return appropriate HTTP status codes for different scenarios (e.g., 400 Bad Request, 404 Not Found, 500 Internal Server Error)

## Requirements
- Python 3.x
- Flask
- Flask_SQLAlchemy

## Installation and Setup
1. **Clone the Repository:**

2. **Install Dependencies:**
   ```sh
   pip install flask flask_sqlalchemy
   ```

3. **Run the Application:**
   ```sh
   python app.py
   ```

## API Endpoints

### Create a New User
- **Endpoint:** `/data/create`
- **Method:** POST
- **Request Body:**
  ```json
  {
    "username": "johndoe",
    "fullname": "John Doe",
    "age": 30,
    "gender": "Male",
    "email": "johndoe@example.com"
  }
  ```
- **Response:** `201 Created`

### Retrieve All Users
- **Endpoint:** `/data`
- **Method:** GET
- **Response:** `200 OK`, returns a JSON array of users

### Retrieve User by ID
- **Endpoint:** `/data/<int:id>`
- **Method:** GET
- **Response:** `200 OK` if user exists, `404 Not Found` otherwise

### Retrieve User by Name
- **Endpoint:** `/data`
- **Method:** GET
- **Query Parameter:** `username`
- **Response:** `200 OK` if user exists, `404 Not Found` otherwise

### Update User by ID
- **Endpoint:** `/data/<int:id>/update`
- **Method:** PUT
- **Request Body:**
  ```json
  {
    "username": "newusername",
    "fullname": "New Name",
    "age": 31,
    "gender": "Male",
    "email": "newemail@example.com"
  }
  ```
- **Response:** `200 OK` if user updated, `404 Not Found` otherwise

### Update User by Name
- **Endpoint:** `/data/update`
- **Method:** PUT
- **Query Parameter:** `username`
- **Request Body:** Same as above
- **Response:** `200 OK` if user updated, `404 Not Found` otherwise

### Delete User by ID
- **Endpoint:** `/data/<int:id>/delete`
- **Method:** DELETE
- **Response:** `204 No Content` if user deleted, `404 Not Found` otherwise

### Delete User by Name
- **Endpoint:** `/data/delete`
- **Method:** DELETE
- **Query Parameter:** `username`
- **Response:** `204 No Content` if user deleted, `404 Not Found` otherwise

## Error Handling
The API includes proper error handling and returns appropriate HTTP status codes:
- `400 Bad Request` for missing or invalid data
- `404 Not Found` if a user is not found
- `500 Internal Server Error` for unexpected server errors


## Example `models.py`
Ensure you have a `models.py` file with the following content:
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UsersDatabase(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    fullname = db.Column(db.String())
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, username, fullname, age, gender, email):
        self.username = username
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'age': self.age,
            'gender': self.gender,
            'email': self.email
        }

    def __repr__(self):
        return f"{self.fullname}:{self.username}"
```

## Author
- Michael Oluseye

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Flask documentation: [Flask](https://flask.palletsprojects.com/)
- SQLAlchemy documentation: [SQLAlchemy](https://www.sqlalchemy.org/)
