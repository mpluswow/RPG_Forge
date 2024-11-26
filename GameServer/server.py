import os
import configparser
from flask import Flask, render_template, current_app
from flask_login import LoginManager
from modules import load_blueprints
from modules.db_models.account import db, Account
from sqlalchemy import create_engine, text

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

# Function to create the database if it does not exist
def create_database():
    try:
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

# Configure the app's database URI with the database name
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create tables if they do not exist
with app.app_context():
    try:
        db.create_all()
        print("Database tables created or already exist.")
    except Exception as e:
        print(f"Error creating tables: {e}")

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redirect unauthorized users to the login page
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    with current_app.app_context():
        return db.session.get(Account, int(user_id)) 

@app.route('/')
def home():
    return render_template('index.html')

# Load and register blueprints
load_blueprints(app)

# Start the server
if __name__ == '__main__':
    app.run(host=config['flask']['host'], port=int(config['flask']['port']))
