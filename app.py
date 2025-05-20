from flask import Flask, jsonify, request, send_file, render_template
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta
from payments.pix import Pix
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' ## endereço do db
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app) ## iniciando o app no db
socketio = SocketIO(app)
#Criando rotas [3 principais]
#rota de pagamento -> valida usuário -> Cria registro dentro do banco de dados e retorna para o user
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json() # request é um objeto converte um corpo de requsição em json
    # validacoes
    if 'value' not in data: 
        return jsonify({"message": "Invalid value"}), 400
    
    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(value=data['value'],      
                          expiration_date=expiration_date)
    
    pix_obj = Pix() # criação do obj classe Pix de pix.py
    data_payment_pix = pix_obj.create_payment()
    new_payment.bank_payment_id = data_payment_pix["bank_payment_id"] #qual coluna eu quero armazenar
    new_payment.qr_code = data_payment_pix["qr_code_path"]

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({"message": "The payment has been created",
                    "payment": new_payment.to_dict()})

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    data = request.get_json()

    # validações -> verifica se essas chaves existem ou não
    if "bank_payment_id" not in data and "value" not in data:
        return jsonify({"message": "Invalid payment data"}), 400

    # confirma se o pagamento foi aprovado ou não
    payment = Payment.query.filter_by(bank_payment_id=data.get("bank_payment_id")).first()
    
    if not payment or payment.paid:
        return jsonify({"message": "Payment not found"}), 404
    if data.get("value") != payment.value:
        return jsonify({"message": "Invalid payment data"}), 400

    payment.paid = True
    db.session.commit() #realiza uma atualização no banco de dados
    socketio.emit(f'payment-confirmed-{payment.id}') # emite uma notiicações para todos os clientes conectados
    return jsonify({"message": "The payment has been confirmed"})

@app.route('/payments/pix/qr_code/<file_name>', methods=["GET"])
def get_image(file_name):
    return send_file(f"static/img/{file_name}.png", mimetype='image/png')

#vizualização do qrcode -> user vai saber em tempo real do pagento | retorno na página 
@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    payment = Payment.query.get(payment_id) # usa o payment_id para identificar o registro la no banco de dados

    if not payment:
        return render_template('404.html')
    
    # Carrega template de tela de confirmação, passo os parâmetros que deveram ser carregados em forma de tag no codigo
    if payment.paid:
        return render_template('confirmed_payment.html',    
                               payment_id=payment.id,
                               value=payment.value)
    # Passando parâmetros do da classe Payment em payment.py ao carregar a tela de pagamento
    return render_template('payment.html',  
                           payment_id=payment.id,   
                           value=payment.value,     
                           host="http://127.0.0.1:5000",    
                           qr_code=payment.qr_code) 

# WebSockets
@socketio.on('connect') # evento do cliente conectar com aplicação
def handle_connect():
    print("Client connected to the server")

@socketio.on('disconnect')
def hadle_disconnect():
    print("Client has disconnected to the server")

# Colocar para rodar, executa o sistema numa eventual importação
if __name__ == '__main__':
    socketio.run(app, debug=True)   