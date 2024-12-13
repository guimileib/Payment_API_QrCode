import sys # essa biblioteca permite que o tests_pix.py ao rodar tenha acesso a todos os outros diretorios, diferente de app.py que esta na raiz do diretorio e não precisa
sys.path.append("../") # vai adicionar todas as pastas antes

import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix() # testar a classe pix

    # create a payment
    payment_info = pix_instance.create_payment(base_dir="../")
    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info

    qr_code_path = payment_info["qr_code_path"]
    os.path.isfile(f'/static/img/{qr_code_path}.png')
