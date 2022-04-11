from datetime import datetime
from api.models.db import db

class Sign(db.Model):
  __tablename__ = 'signs'
  id = db.Column(db.Interger, primary_key=True)
  name = db.Column(db.String(20))
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

  def __repr__(self):
    return f"Sign('{self.id}', '{self.name}'"

  def serialize(self):
    sign = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    return sign 