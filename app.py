# 1.Objetivo - criar uma api rest para livros
# 2.Url base - localhost
# 3.Endpoints -
#   - localhost/livros (GET)
#   - localhost/livros (POST)
#   - localhost/livros/id (GET) 
#   - localhost/livros/id (PUT) 
#   - localhost/livros/id (DELETE) 
# 4.Recursos - livros

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

livros = ""
with open('livros.json', 'r', encoding='utf-8') as f:
    livros = json.load(f)

# GET - consultar  todos
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# GET - consultar  livro por id
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return livro
        
# PUT - editar livro
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# POST - inserir livros
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# DELETE - excluir um livro
@app.route('/livro/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

# Rodando API
app.run(port=5000, host='localhost', debug=True)
