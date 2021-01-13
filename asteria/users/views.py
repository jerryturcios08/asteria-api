from datetime import datetime

from flask import Blueprint, jsonify, request

from asteria.db import db

from .models import User
from .schemas import user_schema

blueprint = Blueprint('users', __name__, url_prefix='/users')


@blueprint.route('/', methods=('POST',))
def create_user():
    """The create_user function allows an HTTP request to send the fields for a User class in order to add a new user
    to the database.

    :return: JSON response based on whether or not a User instance was successfully created.
    """
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    username = request.json['username']
    date_of_birth = request.json['date_of_birth']
    city_of_birth = request.json['city_of_birth']
    email = request.json['email']
    password = request.json['password']
    error = None

    # Checks if any of the fields are missing and sets the error accordingly.
    if not first_name:
        error = 'First name is required.'
    elif not last_name:
        error = 'Last name is required.'
    elif not username:
        error = 'Username is required'
    elif not date_of_birth:
        error = 'Date of birth is required.'
    elif not city_of_birth:
        error = 'City of birth is required.'
    elif not email:
        error = 'Email is required.'
    elif not password:
        error = 'Password is required.'

    # Returns a JSON response indicating if the username or email is not unique
    if User.query.filter_by(username=username).first():
        error = 'Username is not unique. Please enter a different username.'
    elif User.query.filter_by(email=email).first():
        error = 'Email is not unique. Please enter a different email.'

    # Creates the new user if no error is present
    if error is None:
        # Takes the date time string and attempts to convert it over to a datetime instance
        try:
            formatted_date = datetime.strptime(date_of_birth, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({'error': f'{date_of_birth} is not a valid date in the format YYYY-MM-DD HH:MM:SS'})
        else:
            new_user = User(first_name, last_name, username, formatted_date, city_of_birth, email, password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'Successfully created a new user.'})
    else:
        return jsonify({'error': error})


@blueprint.route('/<int:id>/', methods=('GET',))
def get_user(id):
    """The get_user function is used to return a single instance from the users database table using the ID as the
    lookup parameter.

    :param id: The user ID used to get a single instance from the users table
    :return: Single instance of User if found
    """
    user = User.query.get(id)
    return user_schema.jsonify(user)
