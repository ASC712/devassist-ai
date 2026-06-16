from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base de conhecimento
base_conhecimento = {
    "api": "API (Interface de Programação de Aplicações) permite que diferentes sistemas se comuniquem entre si.",
    "git": "Git é um sistema de controle de versão utilizado para rastrear alterações em projetos.",
    "github": "GitHub é uma plataforma para hospedagem e colaboração de projetos utilizando Git.",
    "flask": "Flask é um microframework Python utilizado para desenvolvimento de aplicações web.",
    "python": "Python é uma linguagem de programação versátil e amplamente utilizada em desenvolvimento, automação e IA.",
    "json": "JSON é um formato leve para troca de dados entre aplicações.",
    "html": "HTML é a linguagem utilizada para estruturar páginas web.",
    "css": "CSS é utilizado para estilizar páginas web."
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/processar", methods=["POST"])
def processar():

    dados = request.get_json()

    texto = dados.get("texto", "").lower()
    modo = dados.get("modo", "")

    resposta = ""

    # MENTOR DEV
    if modo == "mentor":

        encontrou = False

        for chave, valor in base_conhecimento.items():

            if chave in texto:
                resposta = valor
                encontrou = True
                break

        if not encontrou:
            resposta = (
                "Não encontrei esse tema na minha base de conhecimento. "
                "Tente perguntar sobre Git, GitHub, API, Flask, Python ou JSON."
            )

    # EXPLICADOR DE CÓDIGO
    elif modo == "codigo":

        explicacoes = []

        if "for" in texto:
            explicacoes.append(
                "FOR: estrutura de repetição utilizada para percorrer elementos."
            )

        if "while" in texto:
            explicacoes.append(
                "WHILE: executa um bloco de código enquanto uma condição for verdadeira."
            )

        if "if" in texto:
            explicacoes.append(
                "IF: estrutura utilizada para tomada de decisões."
            )

        if "def" in texto:
            explicacoes.append(
                "DEF: utilizada para criação de funções."
            )

        if "print" in texto:
            explicacoes.append(
                "PRINT: utilizada para exibir informações na tela."
            )

        if len(explicacoes) == 0:
            resposta = (
                "Não identifiquei estruturas conhecidas para explicar."
            )
        else:
            resposta = "\n\n".join(explicacoes)

    # README
    elif modo == "readme":

        resposta = f"""# Projeto

## Descrição

{texto}

## Tecnologias

- Python
- Flask
- HTML
- CSS

## Instalação

1. Instale o Python
2. Instale o Flask
3. Execute app.py

## Uso

Abra o navegador e utilize a aplicação.

## Autor

Projeto gerado pelo DevAssist AI.
"""

    else:
        resposta = "Modo inválido."

    return jsonify({
        "resposta": resposta
    })


if __name__ == "__main__":
    app.run(debug=True)