from database.db import get_connection


class MedicoModel:
    @classmethod
    def validate_login(cls, username, password):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_medico, clave FROM medicos WHERE usuario = %s", (username,))
                medico_data = cursor.fetchone()
                if medico_data:
                    medico_id, stored_password = medico_data
                    if password == stored_password:
                        return medico_id  # Devolver el id_medico si las credenciales son válidas
                return None  # Devolver None si las credenciales son inválidas
        except Exception as ex:
            raise ex
        finally:
            connection.close()

    @classmethod
    def get_medico_id_by_username(cls, username):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_medico FROM medicos WHERE id_medico = %s", (username,))
                medico_id = cursor.fetchone()
                return medico_id[0] if medico_id else None
        except Exception as ex:
            raise ex
        finally:
            connection.close()
