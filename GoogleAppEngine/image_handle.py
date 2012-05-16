import cgi
import webapp2

from google.appengine.api import users
from google.appengine.ext import db

class Images(db.Model):
    author = db.UserProperty(required=True)
    desc = db.StringProperty(multiline=True, default=None)
    img = db.BlobProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    geo_lat = db.FloatProperty(default=None)
    geo_lng = db.FloatProperty(default=None)


html_image_pick_form = """
<html>
<body>
<form action="/image/upload" enctype="multipart/form-data" method="post">
  <div><label>Description:</label></div>
  <div><textarea name="desc" rows="3" cols="60"></textarea></div>
  <div><label>Pick up a file:</label></div>
  <div><input type="file" name="img"/></div>
  <div><input type="submit" value="upload" /></div>
</form>
</body>
</html>
"""
class image_pick(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html_image_pick_form)
    

class image_upload(webapp2.RequestHandler):
    def post(self):
        desc = self.request.get('desc')
        img = self.request.get('img')
        self.response.out.write(img)


app = webapp2.WSGIApplication([
        ('/image/pick', image_pick),
        ('/image/upload', image_upload)
        ],
                              debug=True)
