import os
from banco import ACADEMIA


def gerar_resposta_mock(mensagem_usuario):
    mensagem = mensagem_usuario.lower()

    if "modalidade" in mensagem or "aula" in mensagem or "oferecem" in mensagem:
        return (
            "Nós oferecemos hidroginástica, natação infantil, natação adulto, "
            "hidroterapia, fisioterapia e taekwondo. "
            "As atividades aquáticas são o foco principal do Espaço Aquático. 🏊"
        )

    if "endereço" in mensagem or "onde fica" in mensagem or "localização" in mensagem:
        return (
            f"O Espaço Aquático fica em {ACADEMIA['contatos']['endereco']}. "
            "Será um prazer receber você para conhecer nossa estrutura de piscina. 🏊"
        )

    if "telefone" in mensagem or "whatsapp" in mensagem or "contato" in mensagem:
        return (
            f"Você pode entrar em contato pelo telefone/WhatsApp "
            f"{ACADEMIA['contatos']['whatsapp']}. "
            "Nossa equipe pode te orientar sobre as aulas na piscina."
        )

    if "matrícula" in mensagem or "matricula" in mensagem or "experimental" in mensagem:
        return (
            "Temos matrícula disponível, mas o valor ainda precisa ser confirmado com a equipe. "
            "Posso encaminhar seu interesse para uma atendente. [AVISAR_ATENDENTE]"
        )

    if "humano" in mensagem or "atendente" in mensagem or "pessoa" in mensagem:
        return (
            "Claro! Vou sinalizar para uma atendente continuar o atendimento com você. "
            "[AVISAR_ATENDENTE]"
        )

    if "horário" in mensagem or "horario" in mensagem:
        return (
            "Os horários das modalidades ainda estão sendo cadastrados. "
            "Nossa equipe pode confirmar a melhor turma para você. "
            "Temos opções voltadas principalmente para atividades na piscina. 🏊"
        )

    if "valor" in mensagem or "preço" in mensagem or "mensalidade" in mensagem:
        return (
            "Os valores ainda estão sendo cadastrados. "
            "A academia pode informar descontos e condições especiais quando disponíveis. "
            "Posso encaminhar você para saber mais sobre as aulas aquáticas. [AVISAR_ATENDENTE]"
        )

    return (
        "Olá! Sou o assistente virtual do Espaço Aquático. "
        "Posso ajudar com informações sobre hidroginástica, natação infantil, natação adulto, "
        "hidroterapia, fisioterapia e taekwondo. "
        "Quer conhecer melhor nossas atividades na piscina?"
    )


def gerar_resposta(mensagem_usuario):
    usar_mock = os.getenv("USE_MOCK_LLM", "false").lower() == "true"

    if usar_mock:
        return gerar_resposta_mock(mensagem_usuario)

    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    modelo = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

    prompt = f"""
Você é o assistente virtual da academia {ACADEMIA["nome"]}.

Informações da academia:
Modalidades: {", ".join(ACADEMIA["modalidades"])}
Telefone: {ACADEMIA["contatos"]["telefone"]}
WhatsApp: {ACADEMIA["contatos"]["whatsapp"]}
Instagram: {ACADEMIA["contatos"]["instagram"]}
Endereço: {ACADEMIA["contatos"]["endereco"]}

Informações ainda pendentes:
- Horários: {ACADEMIA["pendencias"]["horarios"]}
- Valores: {ACADEMIA["pendencias"]["valores"]}
- Matrícula: {ACADEMIA["pendencias"]["matricula"]}

Regras:
1. Responda de forma simpática, curta e profissional.
2. Não invente horários, preços ou valores de matrícula.
3. Caso o cliente pergunte algo ainda não cadastrado, diga que a equipe pode confirmar.
4. Sempre que possível, direcione o cliente para conhecer as atividades aquáticas.
5. Se o cliente demonstrar interesse em matrícula, aula experimental ou atendimento humano, sinalize isso no final usando a tag: [AVISAR_ATENDENTE]
6. Responda em português, exceto se o usuário escrever em inglês. Nesse caso, responda em inglês.

Mensagem do cliente:
{mensagem_usuario}
"""

    resposta = client.responses.create(
        model=modelo,
        input=prompt
    )

    return resposta.output_text