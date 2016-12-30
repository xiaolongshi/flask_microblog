from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from flask_mail import Mail
from .momentjs import momentjs

myapp = Flask(__name__)
myapp.config.from_object('config')
db = SQLAlchemy(myapp)
mail = Mail(myapp)

myapp.jinja_env.globals['momentjs'] = momentjs
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

loginmanager = LoginManager()
loginmanager.init_app(myapp)
loginmanager.login_view = 'login'
oldid = OpenID(myapp, os.path.join(basedir, 'tmp'))

if not myapp.debug:
    #import logging
    #from logging.handlers import SMTPHandler
    #credentials = None
    #if MAIL_USERNAME or MAIL_PASSWORD:
    #    credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    #mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS,
    #                            'microblog failure', credentials)
    #mail_handler.setLevel(logging.ERROR)
    #myapp.logger.addHandler(mail_handler)
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(
    logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    
    myapp.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    myapp.logger.addHandler(file_handler)
    myapp.logger.info('microblog startup')
from app import views, models
