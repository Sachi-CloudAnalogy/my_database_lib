# my_database_lib/__init__.py
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:sfdc@localhost:5432/Microservice'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "secretkey"

db = SQLAlchemy()
