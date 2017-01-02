# -*- conding: utf-8 -*-
WTF_CSRF_ENABLED = True
SECRET_KEY = 'xiaolong'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_reposiitory')
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
# mail server settings
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "ziguangtest@gmail.com" # os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = "ziguangzhiye2011" # os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['ziguangtest@gmail.com']

# pagination
POSTS_PER_PAGE = 3

# whoosh_base
WHOOSH_BASE = os.path.join(basedir, 'search.db')

MAX_SEARCH_RESULTS = 50

# available languages
LANGUAGES = {
        'en': 'English',
        'zh_CN': 'Chinese'
        }

# micorsoft translation service
MS_TRANSLATOR_CLIENT_ID = ''
MS_TRANSLATOR_CLIENT_SECRET = ''

# baidu translation service
BAIDU_TRANSLATOR_CLIENT_ID = ''
BAIDU_TRANSLATOR_CLIENT_SECRET = ''
