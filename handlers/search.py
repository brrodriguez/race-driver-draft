# coding=utf-8
import webapp2
from webapp2_extras import jinja2
import time
from google.appengine.api import users
import google.appengine.ext.ndb as ndb
from models.user import User
from models.driver_offer import Driver_offer


class SearchHandler(webapp2.RequestHandler):
    def get(self):
        id = self.request.GET["id"]
        user = ndb.Key(urlsafe=id).get()
        values = {
            "id": id,
            "user": user
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("search.html", **values))
        return

    def post(self):

        id = self.request.GET["id"]
        user = ndb.Key(urlsafe=id).get()

        experiencia = self.request.get("experiencia", "").strip()
        especialidad = self.request.get("especialidad", "").strip()
        objetivo = self.request.get("objetivo", "").strip()

        if experiencia==None and especialidad=="Ninguna" and objetivo=="Ninguno":
            offers = Driver_offer.query()
        else:
            if experiencia == None and especialidad == "Ninguna" and objetivo != "Ninguno":
                offers = Driver_offer.query(Driver_offer.objetivo==objetivo)
            else:
                if experiencia == None and especialidad != "Ninguna" and objetivo == "Ninguno":
                    offers = Driver_offer.query(Driver_offer.especialidad==especialidad)
                else:
                    if experiencia == None and especialidad != "Ninguna" and objetivo != "Ninguno":
                        offers = Driver_offer.query(Driver_offer.especialidad==especialidad and Driver_offer.objetivo==objetivo)
                    else:
                        if experiencia != None and especialidad == "Ninguna" and objetivo == "Ninguno":
                            offers = Driver_offer.query(Driver_offer.experiencia==experiencia)
                        else:
                            if experiencia != None and especialidad == "Ninguna" and objetivo != "Ninguno":
                                offers = Driver_offer.query(Driver_offer.experiencia==experiencia and Driver_offer.objetivo==objetivo)
                            else:
                                if experiencia != None and especialidad != "Ninguna" and objetivo == "Ninguno":
                                    offers = Driver_offer.query(Driver_offer.experiencia==experiencia and Driver_offer.especialidad==especialidad)
                                else:
                                    if experiencia != None and especialidad != "Ninguna" and objetivo != "Ninguno":
                                        offers = Driver_offer.query(Driver_offer.experiencia==experiencia and Driver_offer.especialidad==especialidad and Driver_offer.objetivo==objetivo)

        values = {
            "draft": offers,
            "user": user,
            "id": id
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("draft.html", **values))
        return


app = webapp2.WSGIApplication([
    ('/search', SearchHandler)
], debug=True)