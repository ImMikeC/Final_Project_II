import uuid
from flask import Blueprint, jsonify, request, Flask
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

bpUser = Blueprint('bpUser', __name__)

@bpUser.route('/users', methods=['GET'])
def all_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200


@bpUser.route('/users/<public_id>', methods=['GET'])
def one_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'}), 403

    user_data = {}
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['profile_id'] = user.profile_id
    user_data['public_id'] = user.public_id

    return jsonify({'user': user_data}), 200


@bpUser.route('/management/create-user', methods=['POST'])
def create_user():
    print("__________________________________________")
    data = request.get_json()
    print(data)
    print("__________________________________________")

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(
        email=data['email'],
        password=hashed_password,
        profile_id=data['profile_id'],
        public_id=str(uuid.uuid4()),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'}), 200

    # user = User()
    # user.email = request.json.get('email')
    # user.password = request.json.get('password')
    # user.profile_id = request.json.get('profile_id')
    # user.save()
    # return jsonify(user.serialize()), 200


@bpUser.route('/management/<email>', methods=['PUT'])
def update_user(email):

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'No email found'})

    #user.password = password
    user.profile_id = 1
    db.session.commit()

    return jsonify({'message': 'Usuario actualizado'})

@bpUser.route('/management/<email>', methods=['DELETE'])
def delete_user(email):

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'Correo no encontrado'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'El usuario ha sido eliminado'})

# @bpUser.route('/users/agendas', methods=['GET'])
# def all_users_with_agendas():
#     users = User.query.all()
#     users = list(map(lambda user: user.serialize_with_agendas(), users))
#     return jsonify(users), 200

# @bpUser.route('/users/agendas/contacts', methods=['GET'])
# def all_users_with_agendas_with_contacts():
#     users = User.query.all()
#     users = list(map(lambda user: user.serialize_with_agendas_with_contacts(), users))
#     return jsonify(users), 200

# @bpUser.route('/users/<int:id>', methods=['GET'])
# def get_user_by_id(id):
#     user = User.query.get(id)
#     return jsonify(user.serialize()), 200

# @bpUser.route('/users/<int:id>/agendas', methods=['GET'])
# def get_user_by_id_with_agendas(id):
#     user = User.query.get(id)
#     return jsonify(user.serialize_with_agendas()), 200


# print(request.json.get('email'))
#     email = User.query.get(email)
#     password = request.json.get('password')
#     users = User()
#     users.email = email
#     # user.agendas.append(agenda)
#     # user.update()

#     return jsonify(users()), 200

# return jsonify(user.serialize_with_users()), 200

# @bpUser.route('/users/<int:id>/agendas/contacts', methods=['GET'])
# def get_user_by_id_with_agendas_with_contacts(id):
#     user = User.query.get(id)
#     return jsonify(user.serialize_with_agendas_with_contacts()), 200


# @bpUser.route('/users/<int:id>/agendas/<int:agendas_id>/contacts', methods=['GET'])
# def get_user_by_id_with_agenda_by_id_with_contacts(id, agendas_id):
#     agenda = Agenda.query.filter_by(users_id=id, id=agendas_id).first()
#     return jsonify(agenda.serialize_with_contacts()), 200
