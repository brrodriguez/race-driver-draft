import webapp2
from google.appengine.ext.ndb import Query
from webapp2_extras import jinja2
from models.user import User
import google.appengine.ext.ndb as ndb
from models.driver_offer import Driver_offer

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        id = self.request.GET["id"]
        user = ndb.Key(urlsafe=id).get()

        values = {
            "user": user,
            "id": id
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("profile.html", **values))
        return

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ('/users/profile', ProfileHandler)
], debug=True)