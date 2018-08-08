import webapp2
import os
import jinja2
import json
import math
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
from models import Restuarant
import base64


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname(__file__) ),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Main_Page( webapp2.RequestHandler ):
    def get( self ):
        current_user = users.get_current_user()
        if not current_user:
            template = jinja_current_directory.get_template("templates/main_page.html")
            jinja_values = {
            'signin_page_url' : users.create_login_url('/'),
            }
            self.response.write( template.render( jinja_values ))
        else:
            #datastore
            current_key = ndb.Key('Restaurant', current_user.user_id() )
            current_restaurant = current_key.get()
            # if not current_visitor:
                # current_Restaurant = Restaurant(key=current_key, name=current_user.nickname(), email=current_user.email(), id=current_user.user_id() )
            # current_visitor.put()

            #display
            template = jinja_current_directory.get_template("templates/main_page.html")
            # jinja_values = {
            # 'name' : current_user.nickname(),
            # 'user_addr' : current_user.email(),
            # 'user_id' : current_user.user_id(),
            # 'signout_page_url' : users.create_logout_url('/'),
            # }
            self.response.write( template.render())



        # start_template = jinja_current_directory.get_template("templates/main_page.html")
        # self.response.write( start_template.render())






#route mapping
app = webapp2.WSGIApplication([
    ('/', Main_Page),

], debug=True)
