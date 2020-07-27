from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)

from application import routes

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

from os import getenv

app.config['SECRET_KEY'] = getenv('SECRET_KEY')
