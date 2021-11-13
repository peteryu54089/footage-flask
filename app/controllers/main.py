from app import app
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.forms.main import FormLogin
from app.models.main import User

@app.route('/')
def index():
    return render_template('main/index.html')

@app.route('/admin')
def admin():
    if not current_user.is_active:
        return redirect(url_for('login'))
    return render_template('main/admin.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user)  
                return redirect(url_for('admin'))
            else:
                flash('Wrong Username or Password')
        else:
            flash('Wrong Username or Password')
    return render_template('main/login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
