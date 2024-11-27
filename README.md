# Payment_QRCODE

## Primeira Rota
Primeiro criamos uma rota que cria o pagamento via pix: **create_payment_pix( )**

## Segunda Rota
Segundo criamos uma rota que confirma esse tipo de pagamento para a instituição que está recebendo o pagamento: **pix_confirmation( )**

## Terceira Rota
Essa é a rota de confirmação do pagamento do qrcode para o usuário, manifestada na função: **payment_pix_page(payment_id)**, na rota eu passo um parâmetro (payment_id) que é o mesmo dentro da função.

![Screenshot teste da terceira rota](https://prnt.sc/00_bpRtWcEnx)
