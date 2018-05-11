#!/usr/bin/env python
# coding=utf-8
# (c) Baltasar 2018 MIT License <baltasarq@gmail.com>

import webapp2
import time
from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import jinja2

import models.user as User
from models.driver_offer import Driver_offer


class EditHandler(webapp2.RequestHandler):
    def get(self):
        try:
            idOffer = self.request.GET['idOffer']
        except:
            self.response.write("Error al recuperar el id de la Oferta")
            return

        idUser = self.request.GET['id']
        user = ndb.Key(urlsafe=idUser).get()

        try:
            offer = ndb.Key(urlsafe=idOffer).get()
        except:
            self.response.write("Error al obtener la Oferta")
            return

        values = {
            "user": user,
            "idUser": idUser,
            "idOffer": idOffer,
            "offer": offer
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("edit.html", **values))

        return

    def post(self):
        try:
            idOffer = self.request.GET['idOffer']
        except:
            idOffer = None

        if not idOffer:
            self.response.write("Error al recuperar el id de la Oferta")
            return

        idUser = self.request.GET['idUser']
        user = ndb.Key(urlsafe=idUser).get()

        # Get ticket to delete by key
        try:
            offer = ndb.Key(urlsafe=idOffer).get()
        except:
            self.response.write("Error al obtener la Oferta")
            return

        offer.especialidad = self.request.get("especialidad", "").strip()
        offer.experiencia = self.request.get("experiencia", "").strip()
        offer.objetivo = self.request.get("objetivo", "").strip()

        # Chk
        if len(offer.experiencia) < 1:
            self.response.write("Experiencia debe contener al menos un carácter.")
            return

        # Save
        Driver_offer.update(offer)
        time.sleep(1)
        self.redirect("/driver_offers/my_offers?id=" + idUser)


app = webapp2.WSGIApplication([
    ("/driver_offers/edit", EditHandler),
], debug=True)
