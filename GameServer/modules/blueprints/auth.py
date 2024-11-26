from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from modules.db_models.account import Account, db
from datetime import datetime

blueprint = Blueprint('auth', __name__, template_folder='../../data/html/auth')

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        new_user = Account(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Account.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            # Update the last_login field
            user.last_login = datetime.utcnow()  # Use UTC time for consistency
            db.session.commit()  # Save the change to the database
            
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('home'))
        flash('Invalid username or password.')
    return render_template('login.html')

@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('auth.login'))
