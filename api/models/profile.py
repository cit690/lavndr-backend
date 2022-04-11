from datetime import datetime
from api.models.db import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    dob = db.Column(db.Integer)
    location = db.Column(db.String)
    vibe_check = db.Column(db.String(200))
    bio = db.Column(db.String(500))
    # signs will be one profile to many signs 
    # db.ForeignKey('sign.id')
    sun_sign = db.Column(db.String())
    moon_sign = db.Column(db.String())
    rising_sign = db.Column(db.String())
    # * replace below code when signs are merged :)
    # sun_sign = db.Column(db.String(), db.ForeignKey('sign.id'))
    # moon_sign = db.Column(db.String(), db.ForeignKey('sign.id'))
    # rising_sign = db.Column(db.String(), db.ForeignKey('sign.id'))q
    profile_picture = db.Column(db.String())
    gender_identity = db.Column(db.String())
    orientation = db.Column(db.String())
    smoke = db.Column(db.Boolean())
    drink = db.Column(db.Boolean())
    four_twenty = db.Column(db.Boolean())
    is_sober = db.Column(db.Boolean())

    def __repr__(self):
      return f"Profile('{self.id}', '{self.name}'"

    def serialize(self):
      profile = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return profile