import cgi
import webapp2

from google.appengine.api import users

class Images(db.Model):
    author = db.UserProperty(required=True)
    desc = db.StringProperty(multiline=True, default=None)
    img = db.BlobProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    geo_lat = db.FloatProperty(default=None)
    geo_lng = db.FloatProperty(default=None)
    



app = webapp2.WSGIApplication([('/image/', MainPage)],
                              debug=True)
