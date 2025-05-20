# API de Pagamento PIX com WebSocket

Esta é uma API REST para processamento de pagamentos PIX com notificações em tempo real utilizando WebSocket. O sistema permite criar pagamentos, gerar QR Codes e confirmar transações de forma assíncrona.

## Funcionalidades

- Criação de pagamentos PIX
- Geração de QR Code para pagamento
- Confirmação de pagamentos em tempo real
- Notificações via WebSocket
- Interface web para acompanhamento do status do pagamento

## Tecnologias Utilizadas

- Python 3.x
- Flask (Framework Web)
- Flask-SocketIO (WebSocket)
- SQLAlchemy (ORM)
- SQLite (Banco de Dados)

## Estrutura do Projeto

```
.
├── app.py              # Arquivo principal da aplicação
├── requirements.txt    # Dependências do projeto
├── static/            # Arquivos estáticos (imagens, CSS, JS)
├── templates/         # Templates HTML
├── payments/          # Módulo de pagamentos
├── repository/        # Camada de acesso ao banco de dados
└── db_models/         # Modelos do banco de dados
```

## Rotas da API

### 1. Criar Pagamento PIX
- **Endpoint**: `/payments/pix`
- **Método**: POST
- **Descrição**: Cria um novo pagamento PIX e retorna os dados do pagamento
- **Corpo da Requisição**:
  ```json
  {
    "value": 100.00
  }
  ```

### 2. Confirmação de Pagamento
- **Endpoint**: `/payments/pix/confirmation`
- **Método**: POST
- **Descrição**: Confirma o pagamento PIX realizado
- **Corpo da Requisição**:
  ```json
  {
    "bank_payment_id": "string",
    "value": 100.00
  }
  ```

### 3. Obter QR Code
- **Endpoint**: `/payments/pix/qr_code/<file_name>`
- **Método**: GET
- **Descrição**: Retorna a imagem do QR Code do pagamento

### 4. Página de Pagamento
- **Endpoint**: `/payments/pix/<payment_id>`
- **Método**: GET
- **Descrição**: Renderiza a página de pagamento com o QR Code

## WebSocket

O sistema utiliza WebSocket para notificações em tempo real:
- Evento de conexão: `connect`
- Evento de desconexão: `disconnect`
- Evento de confirmação de pagamento: `payment-confirmed-{payment_id}`

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando o Projeto

```bash
python app.py
```

O servidor será iniciado em `http://127.0.0.1:5000`

## Banco de Dados

O projeto utiliza SQLite como banco de dados. O arquivo do banco é criado automaticamente na pasta `instance/` quando a aplicação é executada pela primeira vez.

## Testes

Os testes estão localizados na pasta `tests/`. Para executar os testes:

```bash
pytest
```




