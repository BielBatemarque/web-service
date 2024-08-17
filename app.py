from flask import Flask, jsonify, request
from contato import Contato

app = Flask(__name__)

@app.route('/olamundo', methods=['GET'])
def ola_mundo_text():
    return "Olá Mundo", 200, {'Content-Type': 'text/plain'}

@app.route('/olamundo/xml', methods=['GET'])
def ola_mundo_xml():
    return "<mensagem>Olá Mundo</mensagem>", 200, {'Content-Type': 'application/xml'}

@app.route('/olamundo/json', methods=['GET'])
def ola_mundo_json():
    return jsonify(mensagem="Olá Mundo")

@app.route('/olamundo/mensagem', methods=['GET', 'POST'])
def mensagem():
    if request.method == 'POST':
        mensagem = request.form.get('mensagem', '')
        return f"<mensagem>{mensagem}</mensagem>", 200, {'Content-Type': 'application/xml'}
    else:
        return "<mensagem>Sem mensagem</mensagem>", 200, {'Content-Type': 'application/xml'}

@app.route('/contato/xml', methods=['GET'])
def contato_xml():
    contato = Contato(nome='João', telefone='1234-5678', email='joao@example.com')
    return contato.to_json(), 200, {'Content-Type': 'application/xml'}

@app.route('/contato/json', methods=['GET'])
def contato_json():
    contato = Contato(nome='Maria', telefone='8765-4321', email='maria@example.com')
    return contato.to_json()

if __name__ == '__main__':
    app.run(debug=True)