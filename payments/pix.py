# cada metodo tem um arquivo na pasta payments
import uuid
import qrcode
#uso de uuid garante um identificador único para o pagamento via PIX.
class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # criar o pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4()) # conversao obj uuid para str

        # codigo_copia_cola_123
        hash_payment = f'hash_payment_{bank_payment_id}' # O que é gerado dentro da pasta img

        # qr_code
        img = qrcode.make(hash_payment)

        # salvar a imagem como PNG
        img.save(f"static/img/qr_code_payment {bank_payment_id}.png")

        return {"bank_payment_id": bank_payment_id, 
                "qr_code_path":f"qr_code_payment_ {bank_payment_id}"}