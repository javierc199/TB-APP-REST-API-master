from flask import Blueprint, request, jsonify
from models.medico_model import MedicoModel
from models.tokens import generate_token, validate_token

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    # Obtener los datos de inicio de sesión del cuerpo de la solicitud
    data = request.json
    username = data.get('usuario')
    password = data.get('clave')

    # Verificar las credenciales del usuario
    medico_id = MedicoModel.validate_login(username, password)

    if medico_id:
        # Si las credenciales son válidas, generar un token JWT
        token = generate_token(medico_id)
        return jsonify({'token': token}), 200
    else:
        # Si las credenciales son inválidas, devolver un mensaje de error
        return jsonify({'error': 'Credenciales inválidas'}), 401

@login_blueprint.route('/verify-token', methods=['POST'])
def verify_token():
    # Obtener el token JWT del cuerpo de la solicitud
    token = request.json.get('token')

    # Validar el token JWT
    medico_id = validate_token(token)

    if medico_id:
        # Si el token es válido, devolver el ID del médico asociado
        return jsonify({'medico_id': medico_id}), 200
    else:
        # Si el token es inválido o ha expirado, devolver un mensaje de error
        return jsonify({'error': 'Token inválido o expirado'}), 401
