#Classe que armazena todas as informações de pagamento
from repository.database import db

# Tabela que armazena todas as informações
class Payment(db.Model):
    # id, value, paid, bank_payment_id, qr_code, expiration_date
    id = db.Column(db.Integer, primary_key=True) # Integer valores cheios
    value = db.Column(db.Float)# Valores quebrados
    paid = db.Column(db.Boolean, default=False)# False, pois no momento que criou não está pago
    bank_payment_id = db.Column(db.Integer, nullable=True) # Não obrigatório
    qr_code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime) # 2024-01-01 -> Armazena a Hora

    def to_dict(self):
        return{
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_payment_id,
            "qr_code": self.qr_code,
            "expiration_date": self.expiration_date
        }