from flask import Flask, request, jsonify
from twilio.rest import Client

import xml.etree.ElementTree as ET
import os

app = Flask(__name__)
XML_FILE = 'agendamentos.xml'

def carregar_agendamentos():
    if not os.path.exists(XML_FILE):
        return []

    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    agendamentos = []

    for agendamento in root.findall('agendamento'):
        data = agendamento.find('data').text
        nome = agendamento.find('nome').text
        contato = agendamento.find('contato').text
        informacoes = agendamento.find('informacoes').text
        agendamentos.append({
            'data': data,
            'nome': nome,
            'contato': contato,
            'informacoes': informacoes
        })

    return agendamentos

def salvar_agendamentos(agendamentos):
    root = ET.Element('agendamentos')

    for agendamento in agendamentos:
        agendamento_elem = ET.SubElement(root, 'agendamento')
        ET.SubElement(agendamento_elem, 'data').text = agendamento['data']
        ET.SubElement(agendamento_elem, 'nome').text = agendamento['nome']
        ET.SubElement(agendamento_elem, 'contato').text = agendamento['contato']
        ET.SubElement(agendamento_elem, 'informacoes').text = agendamento['informacoes']

    tree = ET.ElementTree(root)
    tree.write(XML_FILE)

@app.route('/agendar', methods=['POST'])
def agendar():
    data = request.json['data']
    nome = request.json['nome']
    contato = request.json['contato']
    informacoes = request.json['informacoes']

    agendamentos = carregar_agendamentos()
    agendamentos.append({'data': data, 'nome': nome, 'contato': contato, 'informacoes': informacoes})
    salvar_agendamentos(agendamentos)

    # Enviar mensagem via WhatsApp (API do WhatsApp)
    # ...

    return jsonify({'status': 'sucesso'})

@app.route('/calendario', methods=['GET'])
def calendario():
    agendamentos = carregar_agendamentos()
    return jsonify(agendamentos)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/editar', methods=['PUT'])
def editar():
    data = request.json['data']
    novo_nome = request.json['nome']
    novo_contato = request.json['contato']
    novas_informacoes = request.json['informacoes']

    agendamentos = carregar_agendamentos()
    for agendamento in agendamentos:
        if agendamento['data'] == data:
            agendamento['nome'] = novo_nome
            agendamento['contato'] = novo_contato
            agendamento['informacoes'] = novas_informacoes
            break

    salvar_agendamentos(agendamentos)
    return jsonify({'status': 'atualizado'})

@app.route('/excluir', methods=['DELETE'])
def excluir():
    data = request.json['data']

    agendamentos = carregar_agendamentos()
    agendamentos = [agendamento for agendamento in agendamentos if agendamento['data'] != data]

    salvar_agendamentos(agendamentos)
    return jsonify({'status': 'excluído'})

TWILIO_ACCOUNT_SID = 'sua_account_sid'
TWILIO_AUTH_TOKEN = 'seu_auth_token'
TWILIO_PHONE_NUMBER = 'seu_numero_twilio'

client = Client()

def enviar_mensagem_whatsapp(nome, contato, informacoes):
    mensagem = f"Agendamento Confirmado:\nNome: {nome}\nContato: {contato}\nInformações: {informacoes}"
    client.messages.create(
        body=mensagem,
        from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
        to=f'whatsapp:{contato}'
    )
