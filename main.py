#PROJETO INTEGRADOR - PLENETA TERRA

from flask import Flask, jsonify, request, make_response
#Importa o banco de dados
from bd import Planeta


#Instanciar o modulo Flask na nossa variavel app
app= Flask('planeta')

#PRIMEIRO MÉDTODO - VISUALIZAR DADOS (GET)
#app.route -> definir que essa função é uma rota para que o flask é um metodo que deve ser executado
@app.route('/planeta', methods= ['GET'])
def get_Planeta():
    return Planeta


#PRIMEIRO MÉTODO PARTE 2 - VISUALIZAR DADOS POR ID (GET / ID)
@app.route('/planeta/<int:id>', methods=['GET'])
def get_carros_id(id):
    for planeta in Carros:
        if planeta.get('id') == id:
            return jsonify(carro)

#SEGUNDO MÉTODO - CRIAR NOVOS DADOS (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro= request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso',
                carro=carro
                )
    )

#TERCEIRO MÉTODO - EDITAR DADOS (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])

if __name__ == "__main__":
    app.run(port=5000, host="localhost")
