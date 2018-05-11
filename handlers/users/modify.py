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


class ModifyHandler(webapp2.RequestHandler):
    def get(self):

        idUser = self.request.GET['id']
        user = ndb.Key(urlsafe=idUser).get()

        values = {
            "user": user,
            "idUser": idUser
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("modify.html", **values))
        return

    def post(self):

        idUser = self.request.GET['idUser']
        user = ndb.Key(urlsafe=idUser).get()

        user.nombre = self.request.get("nombre", "").strip()
        user.nacionalidad = self.request.get("nacionalidad", "").strip()
        user.email = self.request.get("email", "").strip()
        user.sexo = self.request.get("sexo", "").strip()

        # Chk
        if len(user.nombre) < 10:
            self.response.write("Nombre debe contener al menos un carácter.")
            return

        if len(user.email) < 1:
            self.response.write("Email debe contener al menos un carácter.")
            return

        if len(user.sexo) < 1:
            self.response.write("Sexo debe contener al menos un carácter.")
            return

        if len(user.nacionalidad) < 1:
            self.response.write("Nacionalidad debe contener al menos un carácter.")
            return


        # Save
        User.update(user)
        time.sleep(1)
        self.redirect("/users/profile?id=" + idUser)


app = webapp2.WSGIApplication([
    ("/users/modify", ModifyHandler),
], debug=True)