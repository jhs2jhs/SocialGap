import cgi
import webapp2
import logging

from db_model import Images
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
  <div><input type='hidden' name='user_email' value='%s'></div>
  <div><input type="submit" value="upload" /></div>
</form>
</body>
</html>
"""
class image_pick(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        debug(user)
        debug(user.user_id())
        self.response.out.write(html_image_pick_form%(user.nickname(), user.email()))
    

class image_upload(webapp2.RequestHandler):
    def post(self):
        desc = self.request.get('desc')
        img = self.request.get('img')
        user_email = self.request.get('user_email')
        user = User(email=user_email)
        self.response.out.write(user)


app = webapp2.WSGIApplication([
        ('/image/pick', image_pick),
        ('/image/upload', image_upload)
        ],
                              debug=True)
