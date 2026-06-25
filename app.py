import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env antes de importar os outros arquivos
load_dotenv()

from llm import gerar_resposta
from whatsapp import enviar_mensagem_whatsapp, avisar_atendente


app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


@app.route("/", methods=["GET"])
def home():
    return "Chatbot Espaço Aquático rodando!"


@app.route("/chat", methods=["POST"])
def chat_web():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Nenhum dado JSON foi enviado."
        }), 400

    mensagem = dados.get("mensagem", "")

    if not mensagem.strip():
        return jsonify({
            "erro": "A mensagem não pode estar vazia."
        }), 400

    resposta = gerar_resposta(mensagem)

    resposta_limpa = resposta.replace("[AVISAR_ATENDENTE]", "").strip()

    return jsonify({
        "resposta": resposta_limpa
    })


@app.route("/teste", methods=["GET"])
def teste_chat():
    mensagem = request.args.get("mensagem", "")

    if not mensagem.strip():
        return jsonify({
            "erro": "Envie uma mensagem pela URL.",
            "exemplo": "http://localhost:5000/teste?mensagem=Quais modalidades vocês oferecem?"
        }), 400

    resposta = gerar_resposta(mensagem)

    resposta_limpa = resposta.replace("[AVISAR_ATENDENTE]", "").strip()

    return jsonify({
        "mensagem": mensagem,
        "resposta": resposta_limpa
    })


@app.route("/webhook", methods=["GET"])
def verificar_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Token inválido", 403


@app.route("/webhook", methods=["POST"])
def receber_mensagem_whatsapp():
    dados = request.get_json()

    try:
        mensagem = dados["entry"][0]["changes"][0]["value"]["messages"][0]
        numero_cliente = mensagem["from"]
        texto_cliente = mensagem["text"]["body"]

        resposta = gerar_resposta(texto_cliente)

        if "[AVISAR_ATENDENTE]" in resposta:
            avisar_atendente(numero_cliente, texto_cliente)
            resposta = resposta.replace("[AVISAR_ATENDENTE]", "").strip()

        enviar_mensagem_whatsapp(numero_cliente, resposta)

    except Exception as erro:
        print("Erro ao processar mensagem do WhatsApp:", erro)

    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)