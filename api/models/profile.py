from datetime import datetime
from api.models.db import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    # * Properties: 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # sender_id = db.Column(db.Integer, db.ForeignKey('recipients.id'))
    # recipient_id = db.Column(db.Integer, db.ForeignKey('senders.id'))

    # message_id = db.Column(db.Integer, db.ForeignKey('messages.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.String())
    dob = db.Column(db.Integer)
    gender_identity = db.Column(db.String())
    orientation = db.Column(db.String())
    location = db.Column(db.String)
    vibe_check = db.Column(db.String(200))
    bio = db.Column(db.String(500))
    # meal = db.Column('meal', db.Enum('B', 'L', 'D', name='meal_type'))
    sun_sign = db.Column('sun_sign', db.Enum('Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis', name='sun_type'))
    moon_sign = db.Column('moon_sign', db.Enum('Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis', name='moon_type'))
    rising_sign = db.Column('rising_sign', db.Enum('Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis', name='rising_type'))

    profile_picture = db.Column(db.String())
    gender_identity = db.Column(db.String())
    orientation = db.Column(db.String())
    smoke = db.Column(db.Boolean())
    drink = db.Column(db.Boolean())
    four_twenty = db.Column(db.Boolean())
    is_sober = db.Column(db.Boolean())

    # * Relationships:
    # messages = db.relationship("Message", secondary="associations")

    def __repr__(self):
      return f"Profile('{self.id}', '{self.name}'"

    def serialize(self):
      profile = {c.name: getattr(self, c.name) for c in self.__table__.columns}

      messages = [message.serialize() for message in self.messages]  # <=== Associate ===
      profile['messages'] = messages  # <=== Associate  ===

      return profile


# class Recipient(db.Model):
#   __tablename__ = 'recipients'
#   id = db.Column(db.Integer, primary_key=True)

#   messages = db.relationship("Message", secondary="associations")

#   def __repr__(self):
#     return f"Recipients('{self.id}', '{self.recipient}'"

#   def serialize(self):
#     recipient = {c.name: getattr(self, c.name) for c in self.__table__.columns}
#     messages = [message.serialize() for message in self.messages]  # <=== Associate ===
#     recipient['messages'] = messages  # <=== Associate  ===
#     return recipient

# class Sender(db.Model):
#   __tablename__ = 'senders'
#   id = db.Column(db.Integer, primary_key=True)

#   messages = db.relationship("Message", secondary="associations")

#   def __repr__(self):
#     return f"senders('{self.id}', '{self.sender}'"

# def serialize(self):
#     sender = {c.name: getattr(self, c.name) for c in self.__table__.columns}
#     messages = [message.serialize() for message in self.messages]  # <=== Associate ===
#     sender['messages'] = messages  # <=== Associate  ===
#     return sender
