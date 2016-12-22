from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myapp = Flask(__name__)
myapp.config.from_object('config')
db = SQLAlchemy(myapp)

import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

loginmanager = LoginManager()
loginmanager.init_app(myapp)
loginmanager.login_view = 'login'
oldid = OpenID(myapp, os.path.join(basedir, 'tmp'))

from app import views, models
