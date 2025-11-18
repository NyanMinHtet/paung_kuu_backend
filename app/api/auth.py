from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/auth/login', methods=['POST'])
def login():
    return "This will be the login route."
