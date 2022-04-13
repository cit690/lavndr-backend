from datetime import datetime
from api.models.db import db


class Message(db.Model):
  __tablename__ = 'messages'
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(500))
  sent_at = db.Column(db.DateTime, default=datetime.utcnow)
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

# * trying this
  recipient_id = db.Column(db.Integer, db.ForeignKey('recipients.id'))
  sender_id = db.Column(db.Integer, db.ForeignKey('senders.id'))

# * Relationships:
# * trying this
  recipients = db.relationship("Recipient", secondary="associations")
  senders = db.relationship("Senders", secondary="associations")

  def __repr__(self):
    return f"Message('{self.id}', '{self.message}'"

  def serialize(self):
    message = {c.name: getattr(self, c.name) for c in self.__table__.columns}

    return message
    # return{
    #     "id": self.id,
    #     "content": self.content,
    #     "profile_id": self.profile_id,
    #     "sent_at": self.sent_at.strftime('%Y-%m-%d')
    # }

class Association(db.Model):
    __tablename__ = 'associations'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('recipients.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('senders.id'))
    message_id = db.Column(db.Integer, db.ForeignKey('messages.id', ondelete='cascade'))

# * "It seems like a message would link 2 users
# * a sender and a recipient. 
# * And both the sender and the recipient would want access to that message"