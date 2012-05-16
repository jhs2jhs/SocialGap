from google.appengine.ext import db

class Social_Image(db.Model):
    author = db.UserProperty(required=True)
    desc = db.StringProperty(multiline=True, default=None)
    img = db.BlobProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    geo_lat = db.FloatProperty(default=None)
    geo_lng = db.FloatProperty(default=None)
