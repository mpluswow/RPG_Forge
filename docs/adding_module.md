## Add a New Module

This project dynamically loads all Flask blueprints from the `modules/blueprints` directory. 

Follow the steps below to add a new module to the game.

---

### Steps to Add a Module

#### 1. Create a Python File
- Navigate to the `modules/blueprints/` directory.
- Add a new `.py` file named after the functionality of your module (e.g., `profile.py`).

#### 2. Define a Blueprint
Inside your new `.py` file:
- Import the `Blueprint` class from Flask.
- Define a `blueprint` variable, which Flask uses to register the module.
- Specify the `template_folder` for your module's HTML files. The folder path is relative to the module file location.

---

### Example
Here’s an example of a new module:

**File:** `modules/blueprints/profile.py`
```python
from flask import Blueprint, render_template
from flask_login import login_required, current_user

blueprint = Blueprint(
    'profile',  # Unique name for the blueprint
    __name__, 
    template_folder='../../data/html/profile'  # Path to your templates
)

@blueprint.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)
```

#### 3. Add HTML Templates
- Create a corresponding directory in `data/html/` for your module (e.g., `data/html/profile`).
- Add the required HTML files for your blueprint in this directory.

**Example Directory Structure:**

```
project/
├── modules/
│   ├── blueprints/
│   │   ├── profile.py
├── data/
│   ├── html/
│   │   ├── profile/
│   │   │   ├── profile.html
```