from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager() 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = "chave_ultra_secreta"
db.init_app(app)
bcrypt  = Bcrypt(app)
login_manager.init_app(app)

login_manager.login_view = 'page_login'   # evita mensagem de erro crua ao identifcar falta de login, levando o guest para logar
login_manager.login_message  = "Por favor, realize o Log In"
login_manager.login_message_category = 'Info'

from mercado import routes    # importar depois porque o mercado inicializa justamente nesse arquivo __init__.py
