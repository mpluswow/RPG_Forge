from flask_sqlalchemy import SQLAlchemy
import os
import importlib

db = SQLAlchemy()

def load_models():
    models_dir = os.path.join(os.path.dirname(__file__), 'db_models')
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"modules.db_models.{filename[:-3]}"
            importlib.import_module(module_name)

load_models()
