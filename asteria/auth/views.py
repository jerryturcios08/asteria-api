from datetime import datetime, timedelta
from functools import wraps

from flask import Blueprint, current_app, jsonify, make_response, request
from jwt import decode, encode, DecodeError
from werkzeug.security import check_password_hash

from asteria.users.models import User

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login/', methods=('GET', 'POST'))
def login():
    """The login function allows the client to obtain and API token if they successfully logged in using a user's email
    and password. The request must use Basic Auth in the request. The password hash is also verified.

    :return: JSON response dependent on whether a token is created or not
    """
    auth = request.authorization

    # Checks if Basic Auth was used and that a valid username and password is sent
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

    user = User.query.filter_by(email=auth.username).first()

    # Returns a token if the password sent matches the hash of the user's password
    if check_password_hash(user.password, auth.password):
        token = encode(
            {'id': user.id, 'exp': datetime.utcnow() + timedelta(days=12)},
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})


def token_required(func):
    """The token_required function is a decorator which is used on routes that require a user to be authenticated."""
    @wraps(func)
    def decorator(*args, **kwargs):
        token = None

        # Grabs the token from the header parameter of 'x-access-tokens'
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'A valid token is missing.'})

        # Passes the current user to func if the token is valid
        try:
            data = decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(id=data['id']).first()
        except DecodeError:
            return jsonify({'message': 'Token is invalid.'})

        return func(current_user, *args, **kwargs)
    return decorator
