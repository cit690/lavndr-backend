from datetime import datetime
from api.models.db import db
from api.models.message import Message


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
    sun_sign = db.Column(db.String())
    moon_sign = db.Column(db.String())
    rising_sign = db.Column(db.String())
    profile_picture = db.Column(db.String())
    gender_identity = db.Column(db.String())
    orientation = db.Column(db.String())
    smoke = db.Column(db.Boolean())
    drink = db.Column(db.Boolean())
    four_twenty = db.Column(db.Boolean())
    is_sober = db.Column(db.Boolean())

    # * commented out code below is claire's
    # messages = db.relationship("Message", cascade='all')
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')

    messages_received = db.relationship('Message',
                                    foreign_keys='Message.recipient_id',
                                    backref='recipient', lazy='dynamic')

    last_message_read_time = db.Column(db.DateTime)

    def __repr__(self):
      return f"Profile('{self.id}', '{self.name}'"

    def serialize(self):
      profile = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      messages = [message.serialize() for message in self.messages]
      profile['messages'] = messages
      return profile

    def new_messages(self):
      last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
      return Message.query.filter_by(recipient=self).filter(
      Message.timestamp > last_read_time).count()