from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from app.forms.main import FormLogin
from app.models.main import User, Qna, Contact

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('main/index.html', contacts = contacts)

@app.route('/admin')
def admin():
    if not current_user.is_active:
        return redirect(url_for('login'))
    return render_template('main/admin.html')

@app.route('/about')
def about():
    if not current_user.is_active:
        return redirect(url_for('login'))
    return render_template('main/about.html')

@app.route('/projects')
def projects():
    if not current_user.is_active:
        return redirect(url_for('login'))
    return render_template('main/projects.html')

@app.route('/qna', methods = ['GET', 'POST'])
def qna():
    if not current_user.is_active:
        return redirect(url_for('login'))
    if request.method == 'POST':
        Qna.query.delete()
        qnas = list(request.form.listvalues())[:-1]
        for i in range(0, len(qnas), 3):
            db.session.add(Qna(title = qnas[i][0], content = qnas[i + 1][0], category = qnas[i + 2][0]))
        db.session.commit()
        flash('Saved successfully')
    qnas1 = Qna.query.filter_by(category = '1').all()
    qnas2 = Qna.query.filter_by(category = '2').all()
    qnas3 = Qna.query.filter_by(category = '3').all()
    return render_template('main/qna.html', qnas1 = qnas1, qnas2 = qnas2, qnas3 = qnas3)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if not current_user.is_active:
        return redirect(url_for('login'))
    if request.method == 'POST':
        Contact.query.delete()
        contacts = list(request.form.listvalues())[:-1]
        for i in range(0, len(contacts), 2):
            db.session.add(Contact(title = contacts[i][0], content = contacts[i + 1][0]))
        db.session.commit()
        flash('Saved successfully')
    return render_template('main/contact.html', contacts = Contact.query.all())

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
