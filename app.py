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

#vizualização do qrcode -> user vai saber em tempo real do pagento
@app.route('/payments/pix/<int:paymentos_id>', methods=['GET'])
def payments_pix_page(payment_id):
    return 'pagamento pix'

#colocar para rodar, executa o sistema numa eventual importação
if __name__ == '__main__':
    app.run(debug=True)