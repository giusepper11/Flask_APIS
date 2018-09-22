from flask import Flask
from flask import jsonify
from flask import request
import uuid

App = Flask(__name__)

Resposta = {"Status":"", "Dados":"", "Mensagem":""}
Produtos = []

@App.route("/produtos", methods=["GET"])
def ListarProdutos():
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = ""
    Resposta["Dados"] = Produtos
    return jsonify(Resposta)

@App.route("/produtos/cadastrar", methods=["POST"])
def CadastrarProduto():
    Dados = request.get_json()
    Id = str(uuid.uuid1())
    Nome = Dados["Nome"]
    Preco = Dados["Preco"]
    Produtos.append({"Id":Id, "Nome":Nome, "Preco":Preco})
    
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Produto cadastrado."
    Resposta["Dados"] = Produtos
    return jsonify(Resposta)

@App.route("/produtos/excluir/<Id>", methods=["DELETE"])
def ExcluirProduto(Id):

    P = None
    for P in Produtos:
        if P["Id"] == Id:
            Produtos.remove(P)
        else:
            P = None

    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Produto Excluído"
    Resposta["Dados"] = P

    return jsonify(Resposta)

@App.route("/produtos/atualizar", methods=["PUT"])
def AtualizarProduto():
    Dados = request.get_json()
    
    for P in Produtos:
        if P["Id"] == Dados["Id"]:
            P["Nome"] = Dados["Nome"]
            P["Preco"] = Dados["Preco"]
            break
    
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Produto atualizado."
    Resposta["Dados"] = P

    return jsonify(Resposta)

if __name__ == "__main__":
    App.run(port=80)