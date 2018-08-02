import webapp2
import os
import jinja2
import json
import math
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
# from models import
import base64


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname(__file__) ),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Main_Page( webapp2.RequestHandler ):
    def get( self ):
        


        start_template = jinja_current_directory.get_template("templates/main_page.html")
        self.response.write( start_template.render())






#route mapping
app = webapp2.WSGIApplication([
    ('/', Main_Page),

], debug=True)
