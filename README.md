# Payment_QRCODE

## Primeira Rota
Primeiro criamos uma rota que cria o pagamento via pix: **create_payment_pix( )**

## Segunda Rota
Segundo criamos uma rota que confirma esse tipo de pagamento para a instituição que está recebendo o pagamento: **pix_confirmation( )**

## Terceira Rota
Essa é a rota de confirmação do pagamento do qrcode para o usuário, manifestada na função: **payment_pix_page(payment_id)**, na rota eu passo um parâmetro (payment_id) que é o mesmo dentro da função.

![Screenshot_1](https://github.com/user-attachments/assets/1b82f5fe-73c5-474e-8632-a99866c012de)
