from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.profile import Profile

profiles = Blueprint('profiles', 'profiles')

# Creating a profile
# Conceptualize route - Creating profiles


