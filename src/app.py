from flask import Flask
from config import config
from flask_cors import CORS

# Rutas
from routes import paciente_controlador, medico_controlador

app = Flask(__name__)
CORS(app)

# Registra los blueprints para los controladores de pacientes y médicos
app.register_blueprint(paciente_controlador.main, url_prefix='/api/pacientes')
app.register_blueprint(medico_controlador.login_blueprint, url_prefix='/api/medicos')

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

app.config.from_object(config['development'])

if __name__ == '__main__':
    app.run(host='192.168.100.35', port=5000)
