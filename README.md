# Agendamento Salão Social do Condomínio

Este projeto é uma aplicação web para agendamento de horários no salão social de um condomínio. Os usuários podem reservar datas, visualizar um calendário com as datas agendadas e disponíveis, e receber notificações via WhatsApp. O backend é construído em Python usando Flask e o frontend utiliza Bootstrap e Axios.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Python, Flask
- **Banco de Dados**: XML para armazenamento de dados
- **API de Mensagens**: Twilio (para envio de mensagens no WhatsApp)

## Funcionalidades

- **Agendamento**: Permite que os usuários agendem um horário no salão social, preenchendo os campos de nome completo, número de contato e informações adicionais.
- **Calendário**: Exibe um calendário com todas as datas agendadas e as disponíveis.
- **Notificações**: Envia mensagens de confirmação de agendamento via WhatsApp.
- **Edição e Exclusão de Agendamentos**: Os usuários podem editar ou excluir agendamentos existentes.

## Estrutura do Projeto

```
agendacac/
├── app.py               # Código do backend em Python
├── templates/
│   └── index.html      # Página principal do frontend
├── static/
│   ├── script.js        # Código JavaScript para manipulação do DOM
│   └── style.css        # Estilos CSS personalizados
└── data.xml             # Arquivo XML para armazenamento de agendamentos
```

## Uso

- Acesse a página principal onde você poderá visualizar o calendário.
- Para agendar um horário, preencha os campos solicitados e clique no botão de agendamento.
- As confirmações de agendamento serão enviadas via WhatsApp.

## Exemplo de Código

### Backend (app.py)

```python
from flask import Flask, jsonify, request
from twilio.rest import Client
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Simulação de um calendário agendado
calendario = []

@app.route('/calendario', methods=['GET'])
def obter_calendario():
    return jsonify(calendario)

@app.route('/agendar', methods=['POST'])
def agendar():
    # Lógica para agendar uma data
    # Enviar mensagem via WhatsApp usando Twilio
    return jsonify({"message": "Agendamento realizado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
```

### Frontend (index.html)

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agendamento Salão Social</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="static/style.css">
</head>
<body>
    <div class="container">
        <h1>Agende seu horário no Salão Social</h1>
        <!-- Formulário de agendamento -->
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="static/script.js"></script>
</body>
</html>
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para discutir melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
