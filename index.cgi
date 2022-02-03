#!/usr/local/bin/python3
from wsgiref.handlers import CGIHandler
from App import app
CGIHandler().run(app)