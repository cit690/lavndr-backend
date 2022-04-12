from email import message
from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.message import Message
from api.models.profile import Profile

messages = Blueprint('messages', 'message')

# creating a msg
@messages.route('/', methods=["POST"])
@login_required
def create():
  profile = Profile.query.filter_by(name=recipient).first_or_404()
  data = request.get_json()
  # below, we retrieve a user's user data with the read_token middleware function, and assign that to a variable called user
  user = read_token(request)
  data["profile_id"] = user["id"]
  # We pass the updated data dictionary to our Profile model, which creates the new resource in our database.
  message = Message(**data)
  db.session.add(message)
  db.session.commit()
  return jsonify(message.serialize()), 201

# ***** following the tutorial that i sent to claire 
# im on the part where they say
# "Next I'm going to add a new /send_message/<recipient> route"
# they use a flask form but since we're using react, we can try to incorporate those parts in a different way

# @bp.route('/send_message/<recipient>', methods=['GET', 'POST'])
# @login_required
# def send_message(recipient):
#     user = User.query.filter_by(username=recipient).first_or_404()
#     form = MessageForm()
#     if form.validate_on_submit():
#         msg = Message(author=current_user, recipient=user,
#                       body=form.message.data)
#         db.session.add(msg)
#         db.session.commit()
#         flash(_('Your message has been sent.'))
#         return redirect(url_for('main.user', username=recipient))
#     return render_template('send_message.html', title=_('Send Message'),
#                            form=form, recipient=recipient)










# indexing a msg - @login_required
@messages.route('/', methods=["GET"])
@login_required
def index():
  messages = Message.query.all()
  return jsonify([message.serialize() for message in messages]), 200


# show a msg - @login_required
@messages.route('/<id>', methods=["GET"])
@login_required
def show(id):
  message = Message.query.filter_by(id=id).first()
  message_data = message.serialize()
  return jsonify(message=message_data), 200

# update msg
@messages.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  message = Message.query.filter_by(id=id).first()

  if message.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(message, key, data[key])

  db.session.commit()
  return jsonify(message.serialize()), 200

# delete msg
@messages.route('/<id>', methods=["DELETE"]) 
@login_required
def delete(id):
  profile = read_token(request)
  message = Message.query.filter_by(id=id).first()

  if message.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(message)
  db.session.commit()
  return jsonify(message="Success"), 200