import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_migrate import Migrate

from asteria import users
from asteria.auth import views
from asteria.db import db

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
load_dotenv(find_dotenv())

# SQLAlchemy configurations
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Registers view blueprints for each module in the project
app.register_blueprint(auth.views.blueprint)
app.register_blueprint(users.views.blueprint)

if __name__ == '__main__':
    app.run(DEBUG=True)
