from flask import Flask
from flask import jsonify
from flask import request
import uuid

App = Flask(__name__)

Resposta = {"Status": "", "Dados": "", "Mensagem": ""}
Alunos = []


@App.route("/alunos", methods=["GET"])
def ListarAlunos():
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Alunos enviados"
    Resposta["Dados"] = Alunos
    return jsonify(Resposta)


@App.route("/alunos/cadastrar", methods=["POST"])
def CadastrarAluno():
    Dados = request.get_json()
    RA = Dados['RA']
    Nome = Dados["Nome"]
    Ativo = Dados["Ativo"]
    for a in Alunos:
        if RA == a['RA']:
            Resposta["Status"] = "Falha!"
            Resposta["Mensagem"] = "RA já cadastrado."
            Resposta["Dados"] = ''
            return jsonify(Resposta)

    Alunos.append({"RA": RA, "Nome": Nome, "Ativo": Ativo})
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Aluno cadastrado."
    Resposta["Dados"] = Alunos
    return jsonify(Resposta)


@App.route("/alunos/excluir/<RA>", methods=["DELETE"])
def ExcluirAluno(RA):
    for a in Alunos:
        if str(a["RA"]) == RA:
            Alunos.remove(a)
            Resposta["Status"] = "Sucesso"
            Resposta["Mensagem"] = "Aluno Excluído"
            Resposta["Dados"] = a
            return jsonify(Resposta)
    Resposta["Status"] = "Falha!"
    Resposta["Mensagem"] = "Nada foi excluido"
    Resposta["Dados"] = ''
    return jsonify(Resposta)


@App.route("/alunos/atualizar", methods=["PUT"])
def AtualizarAluno():
    Dados = request.get_json()

    for a in Alunos:
        if a["RA"] == Dados["RA"]:
            a["Nome"] = Dados["Nome"]
            a["Ativo"] = Dados["Ativo"]
            Resposta["Status"] = "Sucesso"
            Resposta["Mensagem"] = "Aluno atualizado."
            Resposta["Dados"] = a
            return jsonify(Resposta)

    Resposta["Status"] = "Falha"
    Resposta["Mensagem"] = "Nada foi atualizado."
    Resposta["Dados"] = ''
    return jsonify(Resposta)


@App.route("/alunos/consulta/<RA>", methods=["GET"])
def ConsultarAluno(RA):

    for a in Alunos:
        if str(a["RA"]) == RA:
            Resposta["Status"] = "Sucesso"
            Resposta["Mensagem"] = "Aluno encontrado."
            Resposta["Dados"] = a
            return jsonify(Resposta)

    Resposta["Status"] = "Falha"
    Resposta["Mensagem"] = "Aluno não encontrado."
    Resposta["Dados"] = ''
    return jsonify(Resposta)


if __name__ == "__main__":
    App.run(port=8080)
