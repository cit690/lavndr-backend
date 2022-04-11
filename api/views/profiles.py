from email import message
from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.profile import Profile

profiles = Blueprint('profiles', 'profiles')

# Creating a profile
# Conceptualize route - Creating profiles

# @profiles.route('/', methods=["POST"])
# @login_required
# def create():
#   data = request.get_json()
#   # below, we retrieve a user's user data with the read_token middleware function, and assign that to a variable called user
#   user = read_token(request)
#   data["profile_id"] = user["id"]
#   # We pass the updated data dictionary to our Profile model, which creates the new resource in our database.
#   profile = Profile(**data)
#   db.session.add(profile)
#   db.session.commit()
#   return jsonify(profile.serialize()), 201

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
