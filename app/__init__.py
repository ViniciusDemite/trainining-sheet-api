from flask import Flask
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy


env = dotenv_values('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{env["DB_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from app import views