# 🏊 Chatbot Espaço Aquático

Projeto desenvolvido para a academia **Espaço Aquático**, com o objetivo de automatizar o atendimento inicial dos alunos e interessados em atividades aquáticas.

O chatbot é capaz de responder dúvidas frequentes sobre modalidades, horários, localização, contato e informações gerais da academia, proporcionando um atendimento rápido e eficiente.

---

## 📋 Requisitos

- Linguagem de Programação: Python
- Framework Web: Flask
- Interface Web: HTML, CSS e JavaScript
- Processamento de Linguagem Natural: NLTK
- Base de Conhecimento: Estrutura local contendo perguntas e respostas da academia
- Navegador Web para acesso à interface

---

## ⚙️ Funcionalidades

O chatbot pode responder perguntas relacionadas a:

- 🏊 Hidroginástica
- 🏊‍♂️ Natação Infantil
- 🏊‍♂️ Natação Adulta
- 💆 Hidroterapia
- 📍 Endereço da academia
- 📞 Telefones para contato
- 🕒 Horários de funcionamento
- 📝 Informações para matrícula
- ❓ Dúvidas frequentes dos alunos

---

## 🔄 Fluxo do Chatbot

O sistema segue o seguinte fluxo:

1. O usuário envia uma pergunta pela interface web.
2. A mensagem é processada pelo sistema.
3. O chatbot procura uma resposta na base de conhecimento.
4. Caso encontre uma correspondência, retorna a resposta adequada.
5. Caso não encontre, retorna uma mensagem orientando o usuário a entrar em contato com a academia.

---

## 🏢 Informações da Academia

**Espaço Aquático**

📍 Endereço:

Rua São Mateus, 531  
São Mateus - Juiz de Fora/MG  
CEP: 36025-000

📞 Telefone:

(32) 3303-0388

---

## 🧠 Decisões de Desenvolvimento

### 1. Framework

Foi utilizado o Flask por ser um framework leve, simples e amplamente utilizado para aplicações web em Python.

### 2. Base de Conhecimento

As respostas são armazenadas localmente, permitindo rápida consulta e fácil manutenção das informações da academia.

### 3. Interface

A interface foi desenvolvida utilizando HTML, CSS e JavaScript, oferecendo uma experiência simples e intuitiva para os usuários.

### 4. Escalabilidade

A estrutura do projeto permite futuras integrações com:

- WhatsApp
- Telegram
- Inteligência Artificial
- Banco de Dados
- Sistemas de Matrícula

---

## 🚀 Como Rodar o Projeto

### 1. Tenha o Python instalado

Verifique a instalação:

```bash
python --version
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o servidor Flask

```bash
python app.py
```

### 4. Abra o navegador

Acesse:

```bash
http://localhost:5000
```

---

## 📁 Estrutura do Projeto

```text
chatbot-espaco-aquatico/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## 🔮 Melhorias Futuras

- Integração com WhatsApp
- Integração com Instagram
- Cadastro de alunos
- Agendamento de aulas
- Histórico de conversas
- Uso de IA para respostas mais naturais

---

## 👨‍💻 Desenvolvido por

- Gustavo Pestana

Projeto acadêmico desenvolvido para a academia **Espaço Aquático**.
