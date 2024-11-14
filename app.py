
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.secret_key = 'midoria'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD = 'postgresql',
        user = 'sasuke',
        password = 'postgres',
        server = 'localhost',
        database = 'martial_arts_library'
    )
db = SQLAlchemy(app)
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'