import google.appengine.ext.ndb as ndb


class Driver_offer(ndb.Model):
    username = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    fecha = ndb.DateProperty(auto_now_add=True)
    experiencia = ndb.StringProperty(required=True)
    especialidad = ndb.StringProperty(required=True)
    objetivo = ndb.StringProperty(required=True)

    @ndb.transactional
    def update(offer):
        """Updates a section.

            :param par: The ticket to update.
            :return: The key of the record.
        """
        return offer.put()
