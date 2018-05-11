import google.appengine.ext.ndb as ndb


class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    nombre = ndb.StringProperty(required=True)
    nacionalidad = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    fecha_nac = ndb.StringProperty(required=True)
    sexo = ndb.StringProperty(required=True)


@ndb.transactional
def update(user):
    return user.put()
