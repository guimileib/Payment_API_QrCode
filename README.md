# Payment_QRCODE
Esse código é uma API para noticações em tempo real de pagamento; com protocolo websockets, para fazer a confirmação de um pagamento em tempo real.

## Primeira Rota 
**def create_payment_pix():**
Primeiro criamos uma rota que cria o pagamento via pix: **create_payment_pix( )**

## Segunda Rota
**def pix_confirmation():**
Segundo criamos uma rota que confirma esse tipo de pagamento para a instituição que está recebendo o pagamento: **pix_confirmation( )**

## Terceira Rota
**def get_image(file_name):** 
Essa rota "pega" as imagens do qrcode no caminho static/img para poder se mostrada na tela do usuário. O parâmetro file_name é variável utilizada nesse processo.

## Quarta Rota
def payment_pix_page(payment_id)
Essa é a rota de confirmação do pagamento do qrcode para o usuário, manifestada na função: **payment_pix_page(payment_id)**, na rota eu passo um parâmetro (payment_id) que é o mesmo dentro da função. Dentro dessa mesma função, realizamos o carregamento das páginas de erro 404 em HTML, utilizando o *render_template* da bilbioteca do Flask. Além disso, utilizando a mesma função carregamos a página de confirmação de pagamento, dentro de *render_template* carregamos os parâmetros que serão usados como tag no código.

## WebSockets
Utilizamos WebSockets, para o evento de conexão do cliente com a aplicação ***def handle_connect()***. E com sua desconexão def ***hadle_disconnect()***.




