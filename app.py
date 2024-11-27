from flask import Flask

app = Flask(__name__)

#Criando rotas [3 principais]
#rota de pagamento -> valida usuário -> Cria registro dentro do banco de dados e retorna para o user
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({"message": "The payment has been created"})

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed"})