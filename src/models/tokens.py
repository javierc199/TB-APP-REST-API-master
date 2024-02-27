from models.medico_model import MedicoModel
import jwt
import datetime

# Clave secreta para firmar el token (debe mantenerse segura)
SECRET_KEY = "clave_secreta"

def generate_token(username):
    try:
        # Obtener el ID del médico
        medico_id = MedicoModel.get_medico_id_by_username(username)
        
        # Definir la duración de validez del token (por ejemplo, 1 día)
        expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)

        # Crear el payload del token con el ID del médico y la fecha de expiración
        payload = {
            'medico_id': medico_id,
            'exp': expiration
        }

        # Generar el token JWT
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return token
    except Exception as ex:
        raise ex

def validate_token(token):
    try:
        # Decodificar el token JWT y obtener el payload
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        # Verificar si el token ha expirado
        expiration = datetime.datetime.fromtimestamp(payload['exp'])
        if expiration < datetime.datetime.utcnow():
            return None  # Token expirado

        # Devolver el ID del médico del payload del token
        return payload['medico_id']
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido
    except Exception as ex:
        raise ex
