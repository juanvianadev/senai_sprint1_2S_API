from flask import Flask, jsonify, make_response, request
from bd import Dados

app = Flask("dados")

@app.route("/dados", methods=["GET"])
def getDados():
    return Dados

@app.route("/dados/<int:id>", methods=["GET"])
def getDadosID(id):  
    for dados in Dados:
        if dados.get("id") == id:
            return jsonify(dados)

@app.route("/dados", methods=["POST"])
def inserirDados():
    dado = request.jason
    Dados.append(dado)
    return make_response(
        jsonify(mensagem = "Dado cadastrado com sucesso!" , dado = dado)
    )

@app.route("/dados/<int:id>", methods=["PUT"])
def editarDadosID(id):
    dadoAlterado = request.get_json()
    for indice, dado in enumerate(Dados):
        if dado.get('id') == id:
            Dados[indice].update(dadoAlterado)
            return jsonify(Dados[indice])

@app.route("/dados/<int:id>", methods=["DELETE"])
def excluirDadosID(id):
    for indice, dado in enumerate(Dados):
        if dado.get('id') == id:
            del Dados[indice]
            return make_response(
                jsonify(mensagem = "Dado excluido com sucesso!")
            )

app.run(port=5000, host="localhost")