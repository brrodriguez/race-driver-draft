#!/usr/bin/env python
# (c) Baltasar 2018 MIT License <baltasarq@gmail.com>

import webapp2
import time
from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import jinja2

import models.user as User
from models.driver_offer import Driver_offer


class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        try:
            idOffer = self.request.GET['idOffer']
        except:
            self.response.write("Error al recuperar el id de la Oferta")
            return

        id = self.request.GET['id']
        user = ndb.Key(urlsafe=id).get()

        try:
            offer = ndb.Key(urlsafe=idOffer).get()
        except:
            self.response.write("Error al obtener la Oferta")
            return

        values = {
            "user": user,
            "id": id,
            "idOffer": idOffer,
            "offer": offer
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("delete.html", **values));

        return

    def post(self):
        try:
            idOffer = self.request.GET['idOffer']
        except:
            idOffer = None

        if not idOffer:
            self.response.write("Error al recuperar el id de la Oferta")
            return

        id = self.request.GET['id']
        user = ndb.Key(urlsafe=id).get()


        # Get ticket to delete by key
        try:
            offer = ndb.Key(urlsafe=idOffer).get()
        except:
            self.response.write("Error al obtener la Oferta")
            return

        # Delete
        offer.key.delete()
        time.sleep(1)
        self.redirect("/driver_offers/my_offers?id=" + id)


app = webapp2.WSGIApplication([
    ("/driver_offers/delete", DeleteHandler),
], debug=True)
