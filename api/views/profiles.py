from flask import Blueprint, jsonify, request, session
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.profile import Profile
from api.models.message import Message
from api.models.message import Association

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
  print("hello!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

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
def assoc_toy(cat_id, toy_id):
  data = { "cat_id": cat_id, "toy_id": toy_id }

  profile = read_token(request)
  cat = Cat.query.filter_by(id=cat_id).first()
  
  if cat.profile_id != profile["id"]:
    return 'Forbidden', 403

  assoc = Association(**data)
  db.session.add(assoc)
  db.session.commit()

  cat = Cat.query.filter_by(id=cat_id).first()
  return jsonify(cat.serialize()), 201

# * association route referencegi
# @cats.route('/<cat_id>/toys/<toy_id>', methods=["LINK"]) 
# @login_required
# def assoc_toy(cat_id, toy_id):
#   data = { "cat_id": cat_id, "toy_id": toy_id }

#   profile = read_token(request)
#   cat = Cat.query.filter_by(id=cat_id).first()
  
#   if cat.profile_id != profile["id"]:
#     return 'Forbidden', 403

#   assoc = Association(**data)
#   db.session.add(assoc)
#   db.session.commit()

#   cat = Cat.query.filter_by(id=cat_id).first()
#   return jsonify(cat.serialize()), 201