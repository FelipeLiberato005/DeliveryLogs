from DeliveryEntrega import database, app
from DeliveryEntrega.models import Usuario

with app.app_context():
    database.create_all()