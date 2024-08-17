from flask import jsonify

class Contato:
    def __init__(self, nome='', telefone='', email=''):
        self.nome = nome
        self.telefone = telefone
        self.email = email


    def to_json(self):
        return jsonify({
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email
        })