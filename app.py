from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Importar y registrar blueprints después de inicializar la aplicación
from app.controllers.auth_controller import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run()
