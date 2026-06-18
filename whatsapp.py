import os
import requests

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
ATENDENTE_NUMERO = os.getenv("ATENDENTE_NUMERO")


def enviar_mensagem_whatsapp(numero, mensagem):
    url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {
            "body": mensagem
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def avisar_atendente(numero_cliente, mensagem_cliente):
    if not ATENDENTE_NUMERO:
        return

    mensagem = f"""
Novo atendimento importante no chatbot Espaço Aquático.

Cliente: {numero_cliente}
Mensagem: {mensagem_cliente}

Possível interesse em matrícula, aula experimental ou atendimento humano.
"""

    enviar_mensagem_whatsapp(ATENDENTE_NUMERO, mensagem)