# coding=utf-8
import webapp2
from webapp2_extras import jinja2
import time
import google.appengine.ext.ndb as ndb
from models.user import User


class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        values = {}

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("register.html", **values))
        return

    def post(self):

        username = self.request.get("username", "").strip()
        password = self.request.get("password", "").strip()
        nombre = self.request.get("nombre", "").strip()
        nacionalidad = self.request.get("nacionalidad", "").strip()
        email = self.request.get("email", "").strip()
        fecha_nac = self.request.get("fecha_nac", "").strip()
        sexo = self.request.get("sexo", "").strip()



        user = User(username=username, password=password, nombre=nombre, nacionalidad=nacionalidad, email=email, fecha_nac=fecha_nac, sexo=sexo)
        userR = User.query(ndb.OR(User.username == username))
        emailR = User.query(ndb.OR( User.email == email))

        if userR.count() > 0:
            self.response.write("El nombre de usuario ya está en uso")
            return
        else:
            if emailR.count() > 0:
                self.response.write("El email ya está en uso")
                return
            else:
                user.put()
                time.sleep(1)
                self.redirect("/")

app = webapp2.WSGIApplication([
    ('/register', RegisterHandler)
], debug=True)