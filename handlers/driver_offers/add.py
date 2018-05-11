# coding=utf-8
import webapp2
from webapp2_extras import jinja2
import time
from google.appengine.api import users
import google.appengine.ext.ndb as ndb
from models.user import User
from models.driver_offer import Driver_offer


class AddHandler(webapp2.RequestHandler):
    def get(self):
        id = self.request.GET["id"]
        user = ndb.Key(urlsafe=id).get()
        offers = Driver_offer.query(Driver_offer.username==user.username)

        if offers.count() >= 2:
            self.response.write("No se pueden publicar más de dos ofertas por usuario.")
            return

        values = {
            "user": user,
            "id": id,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("add.html", **values))
        return

    def post(self):
        id = self.request.GET["id"]
        user = ndb.Key(urlsafe=id).get()
        username = user.username
        email = user.email

        experiencia = self.request.get("experiencia", "").strip()
        especialidad = self.request.get("especialidad", "").strip()
        objetivo = self.request.get("objetivo", "").strip()

        if len(experiencia) == 0 or len(especialidad) == 0 or len(objetivo) == 0:
            self.response.write("Se deben cubrir todos los campos para poder publicar la oferta")
            return

        driver_offer = Driver_offer(username=username, email=email, experiencia=experiencia, especialidad=especialidad, objetivo=objetivo)

        driver_offer.put()
        time.sleep(1)
        self.redirect("/draft?id=" + id)
        return


app = webapp2.WSGIApplication([
    ('/driver_offers/add', AddHandler)
], debug=True)