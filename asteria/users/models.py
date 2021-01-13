from werkzeug.security import generate_password_hash

from asteria.db import db


class User(db.Model):
    """The User class is used to define a database table for storing users."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    date_of_birth = db.Column(db.DateTime)
    city_of_birth = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, first_name, last_name, username, date_of_birth, city_of_birth, email, password):
        """Initializes an instance of the User class.

        :param first_name: The user's first name
        :param last_name: The user's last name
        :param date_of_birth: The user's date of birth used to generate the chart
        :param city_of_birth: The city where the user was born
        :param email: The user's email used to login
        :param password: The user's password used to login
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.date_of_birth = date_of_birth
        self.city_of_birth = city_of_birth
        self.email = email
        self.password = generate_password_hash(password)
