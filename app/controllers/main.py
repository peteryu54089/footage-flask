from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('main/index.html')

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    return render_template('main/admin.html')

@app.route('/cms')
def cms():
    return render_template('main/cms.html')
