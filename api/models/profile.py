from datetime import datetime
from api.models.db import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    # * Properties: 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    sender_num = db.Column(db.Integer, unique=True, nullable=False)
    recipient_num = db.Column(db.Integer, unique=True, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String())
    dob = db.Column(db.Integer)
    gender_identity = db.Column(db.String())
    orientation = db.Column(db.String())
    location = db.Column(db.String)
    vibe_check = db.Column(db.String(200))
    bio = db.Column(db.String(500))
    sun_sign = db.Column(db.String())
    moon_sign = db.Column(db.String())
    rising_sign = db.Column(db.String())
    smoke = db.Column(db.Boolean())
    drink = db.Column(db.Boolean())
    four_twenty = db.Column(db.Boolean())
    is_sober = db.Column(db.Boolean())

    # * Relationships:
    messages = db.relationship("Message", secondary="associations")  # <=== Associate ===

    def __repr__(self):
      return f"Profile('{self.id}', '{self.name}'"

    def serialize(self):
      profile = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      messages = [message.serialize() for message in self.messages]  # <=== Associate ===
      profile['messages'] = messages  # <=== Associate  ===
      return profile

