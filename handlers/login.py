
import webapp2
from webapp2_extras import jinja2
from models.user import User


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        values = {}

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("login.html", **values))
        return

    def post(self):
        usernameL = self.request.get("usernameLogin", "").strip()
        passwordL = self.request.get("passwordLogin", "").strip()

        if len(usernameL) == 0 or len(passwordL) == 0:
            self.response.write("Se deben cubrir todos los campos")
            return

        usuario = User.query(User.username == usernameL and User.password == passwordL)

        if usuario.count()==1:
            user_id = usuario.fetch(1)[0].key.urlsafe()
            self.redirect("/draft?id=" + user_id)
            return
        else:
            self.response.write("No existe este usuario")
            return

app = webapp2.WSGIApplication([
    ('/', LoginHandler)
], debug=True)
