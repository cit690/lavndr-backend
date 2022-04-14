from flask import Blueprint, jsonify, request, session
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.profile import Profile
from api.models.message import Message

profiles = Blueprint('profiles', 'profile')

# * show all profs
@profiles.route('/', methods=["GET"])
def index():
  profiles = Profile.query.all()
  return jsonify([profile.serialize() for profile in profiles]), 200

# * show one prof
@profiles.route('/<id>', methods=["GET"])
def show(id):
  profile = Profile.query.filter_by(id=id).first()
  profile_data = profile.serialize()
  return jsonify(profile=profile_data), 200

# * update the prof
@profiles.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  user = read_token(request)
  profile = Profile.query.filter_by(id=id).first()

  if profile.user_id != user["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(profile, key, data[key])
  db.session.commit()
  return jsonify(profile.serialize()), 200

# * delete the prof
@profiles.route('/<id>', methods=["DELETE"])
@login_required
def delete(id):
  user = read_token(request)
  profile = Profile.query.filter_by(id=id).first()

  if profile.user_id != user["id"]:
    return 'Forbidden', 403
  
  db.session.delete(profile)
  db.session.commit()
  return jsonify(message="Success"), 200

profiles.route('<id>/messages')


# * associate msg
@profiles.route('/<profile_id>/messages/<message_id>', methods=["LINK"]) 
@login_required
def assoc_msg(message_id, profile_id):
  print("association route firing!")
  data = { "message_id": message_id, "profile_id": profile_id }
  
  profile = read_token(request)
  profile = Profile.query.filter_by(id=profile_id).first()

  if profile.profile_id != profile["id"]:
    return 'Forbidden', 403

  assocMsg = Message(**data)
  db.session.add(assocMsg)
  db.session.commit()

  profile = Profile.query.filter_by(id=profile_id).first()
  return jsonify(profile.serialize()), 201