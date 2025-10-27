from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect

# Inicializar extensões
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
moment = Moment()
csrf = CSRFProtect()

# Configurar login manager
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'info'
