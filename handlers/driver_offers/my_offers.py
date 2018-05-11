import webapp2
from google.appengine.ext.ndb import Query
from webapp2_extras import jinja2
from models.user import User
import google.appengine.ext.ndb as ndb
from models.driver_offer import Driver_offer

class MyOffersHandler(webapp2.RequestHandler):
    def get(self):
        id = self.request.GET["id"]
        user = ndb.Key(urlsafe=id).get()
        offers = Driver_offer.query(Driver_offer.username == user.username).order(-Driver_offer.fecha)

        values = {
            "user": user,
            "id": id,
            "offers": offers
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("my_offers.html", **values))
        return

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ('/driver_offers/my_offers', MyOffersHandler)
], debug=True)