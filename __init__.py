from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config.from_object('app.config.Config')

# Configuración de la base de datos SQLAlchemy
db = SQLAlchemy(app)

# Importar y registrar blueprints después de inicializar la aplicación
from app.controllers.auth_controller import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

# Importar modelos para que SQLAlchemy pueda crear las tablas
from app.models.task import Task
from app.models.user import User

# Importar servicios
from app.services.auth_service import AuthService
from app.services.task_service import TaskService

# Importar utilidades
from app.utils.errors import not_found_error, bad_request_error, unauthorized_error, internal_server_error
from app.utils.jwt_utils import encode_auth_token, decode_auth_token
