from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
if not database_exists(engine.url):
    create_database(engine.url)
db = SQLAlchemy(app)

from app.models.main import Admin

db.create_all()
db.session.commit()

if not Admin.query.filter_by(username = 'admin').first():
    admin = Admin(username = 'admin', password = 'Ty6Lb!Gn85hQ')
    db.session.add(admin)
    db.session.commit()

from app.controllers import main
