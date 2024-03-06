""" This script is a beginner-friendly Flask web application that serves as a RESTful API for managing users in a MySQL database. It uses Flask-SQLAlchemy, an extension for Flask that simplifies the use of SQLAlchemy, a popular Object Relational Mapper (ORM) for Python.

Here's a summary of the key components and their roles in the code:

Flask: Flask is a lightweight web framework for Python that allows you to build web applications quickly. It's designed to make getting started easy with the ability to scale up to complex applications.
SQLAlchemy: SQLAlchemy is an ORM that provides a high-level, Pythonic interface to SQL databases. It allows you to interact with your database like you would with Python objects, without having to write SQL queries.
Flask-SQLAlchemy: This is an extension for Flask that integrates SQLAlchemy with Flask. It provides a simple way to use SQLAlchemy with Flask applications.
RESTful API: A RESTful API (Representational State Transfer) is a set of rules for building web services. It uses standard HTTP methods like GET, POST, PUT, and DELETE to perform operations on resources, which are usually represented as JSON objects.
User Model: The User class is a representation of a user in the database. It defines the structure of a user with attributes like id, name, and age.
API Endpoints: The script defines several API endpoints:
GET /users: Retrieves all users from the database.
POST /users: Adds a new user to the database.
PUT /users/<int:user_id>: Updates an existing user in the database.
DELETE /users/<int:user_id>: Deletes a user from the database.
Database Initialization: The db.create_all() function is called to create the necessary database tables based on the defined models.
For newbie programmers, this script is a great starting point to learn about web development with Flask, database management with SQLAlchemy, and how to create a RESTful API. It demonstrates the basics of setting up a Flask application, defining a model, creating API routes, and interacting with a database.

The script also includes documentation in the form of comments and docstrings, which explain what each part of the code does. This is crucial for understanding the flow of the application and how to use the API endpoints.

In summary, this script is a practical example of how to build a simple web application that can manage users in a database, using Flask and SQLAlchemy to handle the web server and database operations, respectively. It's a great resource for anyone looking to learn more about web development and database management in Python. 

Documentation was created by Phind-34B model."""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and configure the database connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/test'
db = SQLAlchemy(app)

# Define the User model with id, name, and age attributes
class User(db.Model):
    """
    User model representing a user in the database.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        age (int): The age of the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        """
        Convert the User object to a JSON serializable format.

        Returns:
            dict: A dictionary containing the user's id, name, and age.
        """
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

# Define the API endpoint for retrieving all users
@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve all users from the database.

    Returns:
        json: A JSON array of all users.

    Example:
        curl -X GET http://localhost:5000/users
    """
    users = User.query.all()
    return jsonify([user.to_json() for user in users])

# Define the API endpoint for adding a new user
@app.route('/users', methods=['POST'])
def add_user():
    """
    Add a new user to the database.

    Request Body:
        {
            "name": "John Doe",
            "age": 30
        }

    Returns:
        json: The newly created user's data.
        status code: 201 if successful.

    Example:
        curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","age":30}' http://localhost:5000/users
    """
    data = request.get_json()
    new_user = User(name=data['name'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_json()), 201

# Define the API endpoint for updating an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update an existing user in the database.

    Parameters:
        user_id (int): The ID of the user to update.

    Request Body:
        {
            "name": "Jane Doe",
            "age": 28
        }

    Returns:
        json: The updated user's data.

    Example:
        curl -X PUT -H "Content-Type: application/json" -d '{"name":"Jane Doe","age":28}' http://localhost:5000/users/1
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    data = request.get_json()
    user.name = data['name']
    user.age = data['age']
    db.session.commit()
    return jsonify(user.to_json())

# Define the API endpoint for deleting a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user from the database.

    Parameters:
        user_id (int): The ID of the user to delete.

    Returns:
        json: A message indicating the user was deleted.

    Example:
        curl -X DELETE http://localhost:5000/users/1
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})

# Create the database tables if they do not exist
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)