from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

recipes = {
    "Brigadeiro": {
        "ingredients": "1 lata de leite condensado, 2 colheres de sopa de manteiga, 4 colheres de sopa de chocolate em pó, Granulado para decorar",
        "steps": [
            "Em uma panela, misture o leite condensado, a manteiga e o chocolate em pó.",
            "Cozinhe em fogo médio, mexendo sempre, até desgrudar do fundo.",
            "Deixe esfriar, modele em bolinhas e passe no granulado."
        ]
    },
    "Camarão Internacional": {
        "ingredients": "2 xícaras de arroz cozido, 200g de camarões, 1 dente de alho picado, 2 colheres de sopa de manteiga, 1 caixinha de creme de leite, 50g de queijo parmesão ralado, Batata palha para finalizar",
        "steps": [
            "Cozinhe o arroz e reserve.",
            "Refogue o alho na manteiga e adicione os camarões, temperando com sal e pimenta.",
            "Misture o arroz cozido com o creme de leite e o queijo parmesão.",
            "Coloque em um refratário, cubra com queijo parmesão e leve ao forno para gratinar.",
            "Sirva com batata palha por cima."
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    if msg.lower() in recipes:
        recipe = recipes[msg]
        send(f"Com os ingredientes que você tem, que tal fazer um delicioso {msg}? 😋")
        send(f"Ingredientes necessários: {recipe['ingredients']}")
        for step in recipe['steps']:
            send(step)
        send("Prontinho! Agora é só aproveitar sua receita! 🍽️🎉")
    else:
        send("Desculpe, não encontrei uma receita com esses ingredientes. Tente outro nome de prato!")

if __name__ == '__main__':
    socketio.run(app, debug=True)
