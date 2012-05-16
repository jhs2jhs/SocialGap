import cgi
import webapp2
import logging

from db_model import Social_Image
from myutil import debug

from google.appengine.api import users
from google.appengine.api.users import User
from google.appengine.ext import db

html_image_pick_form = """
<html>
<body>
<div>Welcome, %s <div>
<form action="/image/upload" enctype="multipart/form-data" method="post">
  <div><label>Description:</label></div>
  <div><textarea name="desc" rows="3" cols="60"></textarea></div>
  <div><label>Pick up a file:</label></div>
  <div><input type="file" name="img"/></div>
  <div>Lat:<input type='text' name='geo_lat'></input></div>
  <div>Lng:<input type='text' name='geo_lng'></input></div>
  <div><input type='hidden' name='user_email' value='%s'></div>
  <div><input type="submit" value="upload" /></div>
</form>
</body>
</html>
"""
class social_image_pick(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        debug(user)
        debug(user.user_id())
        self.response.out.write(html_image_pick_form%(user.nickname(), user.email()))
    

class social_image_upload(webapp2.RequestHandler):
    def post(self):
        desc = self.request.get('desc')
        img = self.request.get('img')
        geo_lat = self.request.get('geo_lat')
        geo_lng = self.request.get('geo_lng')
        user_email = self.request.get('user_email')
        user = User(email=user_email)
        si = Social_Image(author=user)
        si.desc = desc
        si.img = db.Blob(img)
        si.geo_lat = None
        si.geo_lng = None
        si.put()
        self.response.out.write(user)

class social_image_list(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        debug(user)
        imgs = Social_Image.all()
        imgs.filter('author = ', user)
        debug(str(imgs.count()))
        debug('hello')
        self.response.out.write(imgs)


app = webapp2.WSGIApplication([
        ('/image/pick', social_image_pick),
        ('/image/upload', social_image_upload),
        ('/image/list', social_image_list)
        ],
                              debug=True)
