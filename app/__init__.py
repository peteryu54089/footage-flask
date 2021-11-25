from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)
login = LoginManager(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
if not database_exists(engine.url):
    create_database(engine.url)
db = SQLAlchemy(app)

from app.models.main import User, Qna, Contact

db.create_all()
db.session.commit()

if not User.query.filter_by(username = 'admin').first():
    user = User(username = 'admin', password = 'Ty6Lb!Gn85hQ')
    db.session.add(user)
    db.session.commit()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from app.controllers import main
