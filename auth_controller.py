from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Aquí irá la lógica para la autenticación
    pass
