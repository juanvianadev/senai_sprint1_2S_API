from flask import Flask, jsonify, make_response, request
from bd import Carros

app = Flask("carros")

@app.route("/carros", methods=["GET"])
def getCarros():
    return Carros

@app.route("/carros/<int:id>", methods=["GET"])
def getCarrosID(id):
    for carro in Carros:
        if carro.get("id") == id:
            return jsonify(carro)
        
@app.route("/carros", methods=["POST"])
def criarCarros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem = "Carro cadastrado com sucesso!" , carro = carro)
    )

@app.route("/carros/<int:id>", methods=["PUT"])
def editarCarrosID(id):
    carroAlterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carroAlterado)
            return jsonify(Carros[indice])

@app.route("/carros/<int:id>", methods=["DELETE"])
def excluirCarrosID(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return make_response(
                jsonify(mensagem = "Carro excluido com sucesso!")
            )

app.run(port=5000, host="localhost")