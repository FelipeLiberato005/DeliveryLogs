#criando o app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "d8249cf754448f51ba4174e24349a79c"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from DeliveryEntrega import routes



