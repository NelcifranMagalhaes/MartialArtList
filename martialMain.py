from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db, app
from views_user import *
from views_martial_art import *
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    app.run(debug=True)