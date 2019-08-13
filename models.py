from google.appengine.ext import ndb

class Post(ndb.Model):
    subject = ndb.StringProperty()
    title = ndb.StringProperty()
    content = ndb.StringProperty()
    name = ndb.StringProperty()
    date = ndb.DateProperty(auto_now_add = True)
