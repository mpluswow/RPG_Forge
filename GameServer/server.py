import os
import configparser
from flask import Flask
from modules import load_blueprints
from modules.models import db
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import sys

# Load configuration
config = configparser.ConfigParser()
config.read('conf/server.conf')

# Database configuration parameters
db_username = config['database']['username']
db_password = config['database']['password']
db_host = config['database']['host']
db_port = config['database']['port']
db_name = config['database']['database']

# Create the Flask app
app = Flask(
    __name__,
    static_folder='data',
    template_folder='data/html'
)

# Set secret key
app.secret_key = config['flask']['secret_key']

# Function to create database if it does not exist
def create_database():
    try:
        # Connection string without specifying the database
        connection_string = f"mysql://{db_username}:{db_password}@{db_host}:{db_port}/"
        engine = create_engine(connection_string)
        conn = engine.connect()

        # Execute SQL to create the database if it doesn't exist
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{db_name}`"))
        conn.close()
        engine.dispose()
        print(f"Database '{db_name}' ensured to exist.")
    except Exception as e:
        print(f"Error creating database: {e}")

# Ensure the database exists
create_database()

# Now configure the app's database URI with the database name
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Create tables if they do not exist
with app.app_context():
    try:
        db.create_all()
        print("Database tables created or already exist.")
    except Exception as e:
        print(f"Error creating tables: {e}")

# Load and register blueprints
load_blueprints(app)

if __name__ == '__main__':
    app.run(host=config['flask']['host'], port=int(config['flask']['port']))
