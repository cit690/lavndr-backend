from datetime import datetime
from api.models.db import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    # * Properties: 
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

    # * Relationships:
    # Add association table relationship - using cat/toy relationship example
    # below is old code
    # messages = db.relationship("Message", cascade='all')
    messages = db.relationship("Message", secondary="associations") 

    def __repr__(self):
      return f"Profile('{self.id}', '{self.name}'"

    def serialize(self):
      profile = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      messages = [message.serialize() for message in self.messages]
      profile['messages'] = messages
      return profile

# # todo:
# done
# # add a new relationship 
# # like the one in the cat model under the 'associate toys' section
# # example:
# #  toys = db.relationship("Toy", secondary="associations") # <=== Here ===
# # todo:
# done
# # add to serialize function
# # example:
# # toys = [toy.serialize() for toy in self.toys] # <=== Here ===
#       # cat['feedings'] = feedings
#       # cat['toys'] = toys