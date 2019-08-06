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
    secondTemplate = jinja_current_directory.get_template('templates/digitalArtPage.html')
    self.response.write(secondTemplate.render())

class PollutionHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('templates/pollutionPage.html')
    self.response.write(secondTemplate.render())

class LearningHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('templates/learningPage.html')
    self.response.write(secondTemplate.render())

class AboutHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('templates/about.html')
    self.response.write(secondTemplate.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    #('/cssi', CSSIHandler),
    ('/about', AboutHandler),
    #('/photos', PhotosHandler),
    ('/page1', Page1Handler)
    #'/page2', Page2Handler),
    #('/page3', Page3Handler),
], debug = True)
