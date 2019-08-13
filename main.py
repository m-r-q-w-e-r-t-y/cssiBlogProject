import webapp2
import jinja2
import os
import datetime
from datetime import date
from google.appengine.ext import ndb
from google.appengine.api import users
from models import Post

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
  def get(self):
    blog_posts = Post.query().fetch()
    template_vars = {
        # 'username': name_input,
        'blog_posts': blog_posts
    }
    template = jinja_current_directory.get_template('main.html')
    self.response.write(template.render(template_vars))

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template('new_post.html')
        self.response.write(template.render())
    # This is an alternative way of completing this exercise that doesn't
    # use the Author Model.
    def post(self):
        # Get a list of all previously created blog posts
        blog_posts = Post.query().fetch()
        # Use the user input to create a new blog post
        subject_choice = self.request.get('subject')
        title_input = self.request.get('title')
        content_input = self.request.get('content')
        name_input = self.request.get('name')
        date_posted = date.today()

        blog_post = Post(subject=subject_choice,
                         title=title_input,
                         content=content_input,
                         name=name_input,
                         date=date_posted)
        blog_post.put()

        # Add the new post to the beginning of our already-queried list of
        # posts
        blog_posts.insert(0, blog_post)

        # Render the template
        template_vars = {
            'username': name_input,
            'blog_posts': blog_posts
        }
        template = jinja_current_directory.get_template(
            'main.html')
        self.response.write(template.render(template_vars))

class DigitalHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('digital.html')
    self.response.write(secondTemplate.render())

class LearnHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('learning.html')
    self.response.write(secondTemplate.render())

class PollutionHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('pollution.html')
    self.response.write(secondTemplate.render())

class AboutHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('about.html')
    self.response.write(secondTemplate.render())

class PhotosHandler(webapp2.RequestHandler):
  def get(self):
    secondTemplate = jinja_current_directory.get_template('photos.html')
    self.response.write(secondTemplate.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/posts', BlogHandler),
    ('/pollution', PollutionHandler),
    ('/about', AboutHandler),
    ('/photos', PhotosHandler),
    ('/learning', LearnHandler),
    ('/digital', DigitalHandler)
], debug = True)
