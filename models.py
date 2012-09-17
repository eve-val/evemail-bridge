from google.appengine.ext import db

class Configuration(db.Model):
  key_id = db.IntegerProperty(required=True)
  vcode = db.StringProperty(required=True)
  rcpt_char = db.IntegerProperty(required=True)
  rcpt_org = db.IntegerProperty(required=True)
  rcpt_org2 = db.IntegerProperty()
  dest_email = db.EmailProperty(required=True)

class SeenMail(db.Model):
  mail_id = db.IntegerProperty(required=True)
