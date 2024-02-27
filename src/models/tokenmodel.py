from database.db import get_connection

class TokenModel:
    @classmethod
    def save_token(cls, id_medico, token):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO auth_tokens (id_medico, token) VALUES (%s, %s)", (id_medico, token))
                connection.commit()
        except Exception as ex:
            # Manejar la excepción apropiadamente
            raise ex
        finally:
            connection.close()

    @classmethod
    def delete_token(cls, token):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM auth_tokens WHERE token = %s", (token,))
                connection.commit()
        except Exception as ex:
            # Manejar la excepción apropiadamente
            raise ex
        finally:
            connection.close()

    @classmethod
    def get_id_medico_by_token(cls, token):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_medico FROM auth_tokens WHERE token = %s", (token,))
                id_medico = cursor.fetchone()
                return id_medico[0] if id_medico else None
        except Exception as ex:
            # Manejar la excepción apropiadamente
            raise ex
        finally:
            connection.close()
