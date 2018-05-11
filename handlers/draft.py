import webapp2
from google.appengine.ext.ndb import Query
from webapp2_extras import jinja2
from models.user import User
import google.appengine.ext.ndb as ndb
from models.driver_offer import Driver_offer

class DraftHandler(webapp2.RequestHandler):
    def get(self):
        id = self.request.GET["id"]
        user = ndb.Key(urlsafe=id).get()
        draft = Driver_offer.query().order(-Driver_offer.fecha)

        values = {
            "user": user,
            "id": id,
            "draft": draft
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("draft.html", **values))
        return

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ('/draft', DraftHandler)
], debug=True)