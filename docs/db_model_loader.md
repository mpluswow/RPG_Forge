# Dynamic Database Model Loader

[DB Model Loader](../GameServer/modules/models.py)

This module [DB Model Loader](../GameServer/modules/models.py) is designed to dynamically load and register database models from the `db_models` directory. 
It simplifies model management by automatically discovering and importing model files, ensuring they are integrated with SQLAlchemy.

## How It Works

1. **Dynamic Discovery**:
   - The `load_models` function scans the `db_models` subdirectory within the `modules` package for `.py` files.

2. **Dynamic Importing**:
   - For each `.py` file found, the module name is dynamically constructed and imported using `importlib.import_module`.

3. **SQLAlchemy Initialization**:
   - The `db` object is created as an instance of `SQLAlchemy`.
   - Models are automatically registered with the database through SQLAlchemy when imported.




### Example Model File

Create a new `.py` file in the `db_models` directory (e.g., `user.py`) with the following structure:

```python
from modules import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

## Troubleshooting

- Check for any errors in the console if a model fails to load.
