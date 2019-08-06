import webapp2
import os
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
  def get(self):
    mainTemplate = jinja_current_directory.get_template('templates/main.html')
    self.response.write(mainTemplate.render())

class DigitalHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('templates/digital.html')
    self.response.write(secondTemplate.render())

class LearnHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('templates/learn.html')
    self.response.write(secondTemplate.render())

class PollutionHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('templates/pollution.html')
    self.response.write(secondTemplate.render())

class AboutHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('templates/about.html')
    self.response.write(secondTemplate.render())

class PhotosHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('templates/photos.html')
    self.response.write(secondTemplate.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/pollution', PollutionHandler),
    ('/about', AboutHandler),
    ('/photos', PhotosHandler),
    ('/learn', LearnHandler),
    ('/digital', DigitalHandler)
], debug = True)
