from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.profile import Profile

profiles = Blueprint('messages', 'message')

# creating a msg
@profiles.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  # below, we retrieve a user's user data with the read_token middleware function, and assign that to a variable called user
  user = read_token(request)
  data["profile_id"] = user["id"]
  # We pass the updated data dictionary to our Profile model, which creates the new resource in our database.
  message = Message(**data)
  db.session.add(message)
  db.session.commit()
  return jsonify(message.serialize()), 201

