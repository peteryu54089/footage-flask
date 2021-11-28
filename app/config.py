import os

class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'footage.db')
    SECRET_KEY = b'\xb9k\xdf@\x0e\x1f(\xf2\xb0\xd0\xcb?Y\xdcN\x19G\x12e\xa8\x8b\xe5\xccS'
    SESSION_PROTECTION = 'strong'
    UPLOAD_PROJECTS_1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/images/projects-1/')
    UPLOAD_PROJECTS_2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/images/projects-2/')
