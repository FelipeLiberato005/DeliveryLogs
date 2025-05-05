#banco de dados
from sqlalchemy.testing.pickleable import User
from datetime import datetime
from DeliveryEntrega import database, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.query.get(int(usuario_id))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String(50), nullable=False)


class logLogin(database.Model, UserMixin):
        id = database.Column(database.Integer, primary_key=True)
        usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'))
        ip = database.Column(database.String(50))
        data_hora = database.Column(database.DateTime, default=datetime.utcnow)
        sucesso = database.Column(database.Boolean)
        motivo = database.Column(database.String(100))