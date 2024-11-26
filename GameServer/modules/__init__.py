import os
import importlib

def load_blueprints(app):
    blueprints_dir = os.path.join(os.path.dirname(__file__), 'blueprints')
    for filename in os.listdir(blueprints_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"modules.blueprints.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, 'blueprint'):
                app.register_blueprint(module.blueprint)
