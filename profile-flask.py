#!flask/bin/python
from werkzeug.contrib.profiler import ProfilerMiddleware
from app import myapp

myapp.config['PROFILE'] = True
myapp.wsgi_app = ProfilerMiddleware(myapp.wsgi_app, restrictions=[30])
myapp.run(debug = True)
