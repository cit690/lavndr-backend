from datetime import datetime
from api.models.db import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    # * Properties: 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # old code - keeping just in case
    # sender_num = db.Column(db.Integer, unique=True, nullable=False)
    # recipient_num = db.Column(db.Integer, unique=True, nullable=False)
    # * ok now senders and recipients have their own models & tables instead of unique properties so that they can have an id
    sender_id = db.Column(db.Integer, db.ForeignKey('recipients.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('senders.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String())
    dob = db.Column(db.Integer)
    gender_identity = db.Column(db.String())
    orientation = db.Column(db.String())
    location = db.Column(db.String)
    vibe_check = db.Column(db.String(200))
    bio = db.Column(db.String(500))
    sun_sign = db.Column(db.Enum('Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis'))
    moon_sign = db.Column(db.Enum('Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis'))
    rising_sign = db.Column(db.Enum('Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis'))
    profile_picture = db.Column(db.String())
    gender_identity = db.Column(db.String())
    orientation = db.Column(db.String())
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


class Recipient(db.Model):
  __tablename__ = 'recipients'
  id = db.Column(db.Integer, primary_key=True)

  def __repr__(self):
    return f"Recipients('{self.id}', '{self.message}'"

  def serialize(self):
    return{
        "id": self.id,
        "content": self.content,
        "profile_id": self.profile_id,
        "sent_at": self.sent_at.strftime('%Y-%m-%d')
    }

class Sender(db.Model):
  __tablename__ = 'Senders'
  id = db.Column(db.Integer, primary_key=True)


