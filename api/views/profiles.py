from email import message
from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.profile import Profile
from api.models.message import Message

profiles = Blueprint('profiles', 'profile')

@profiles.route('/', methods=["GET"])
def index():
  profiles = Profile.query.all()
  return jsonify([profile.serialize() for profile in profiles]), 200

@profiles.route('/<id>', methods=["GET"])
def show(id):
  profile = Profile.query.filter_by(id=id).first()
  profile_data = profile.serialize()
  return jsonify(profile=profile_data), 200


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


# profiles.route('<id>/messages', methods=["POST"])
# @login_required
# def create_message(id):
#   data = request.get_json()
#   data["profile_id"] = id

#   profile = read_token(request)
#   profile = Profile.query.filter_by(id=id).first()

#   message = Message(**data)

#   db.session.add(message)
#   db.session.commit()

#   profile_data = profile.serialize()
#   return jsonify(profile_data), 201

