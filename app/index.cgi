#!/home/miyablo/.pyenv/versions/3.7.0/bin/python

import cgitb
cgitb.enable()

from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)