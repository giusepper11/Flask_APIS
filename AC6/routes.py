from server import App
from flask import jsonify
from flask import request
# Models
from Models.resposta import Resposta
# Servicos
from Services.listar import Listar
from Services.cadastar import Cadastrar
from Services.excluir import ExcluirAluno
from Services.atualizar import AtualizarAluno
from Services.consultar import ConsultarAluno


@App.route("/alunos", methods=["GET"])
def ListarRoute():
    Resposta["Status"] = "Sucesso"
    Resposta["Mensagem"] = "Alunos enviados"
    Resposta["Dados"] = Listar()
    return jsonify(Resposta)


@App.route("/alunos/cadastrar", methods=["POST"])
def CadastrarRoute():
    Dados = request.get_json()
    result, alunos = Cadastrar(Dados)
    if not result:
        Resposta["Status"] = "Falha!"
        Resposta["Mensagem"] = "RA já cadastrado."
        Resposta["Dados"] = ''
        return jsonify(Resposta)
    else:
        Resposta["Status"] = "Sucesso"
        Resposta["Mensagem"] = "Aluno cadastrado."
        Resposta["Dados"] = alunos
        return jsonify(Resposta)


@App.route("/alunos/excluir/<RA>", methods=["DELETE"])
def ExcluirRoute(RA):
    result, alunos = ExcluirAluno(RA)
    if result:
        Resposta["Status"] = "Sucesso"
        Resposta["Mensagem"] = "Aluno Excluído"
        Resposta["Dados"] = alunos
        return jsonify(Resposta)
    else:
        Resposta["Status"] = "Falha!"
        Resposta["Mensagem"] = "Nada foi excluido"
        Resposta["Dados"] = ''
        return jsonify(Resposta)


@App.route("/alunos/atualizar", methods=["PUT"])
def AtualizarRoute():
    Dados = request.get_json()
    result, alunos = AtualizarAluno(Dados)
    if result:
        Resposta["Status"] = "Sucesso"
        Resposta["Mensagem"] = "Aluno atualizado."
        Resposta["Dados"] = alunos
        return jsonify(Resposta)
    else:
        Resposta["Status"] = "Falha"
        Resposta["Mensagem"] = "Nada foi atualizado."
        Resposta["Dados"] = ''
        return jsonify(Resposta)


@App.route("/alunos/consulta/<RA>", methods=["GET"])
def ConsultarRoute(RA):
    result, aluno = ConsultarAluno(RA)
    if result:
        Resposta["Status"] = "Sucesso"
        Resposta["Mensagem"] = "Aluno encontrado."
        Resposta["Dados"] = aluno
        return jsonify(Resposta)
    else:
        Resposta["Status"] = "Falha"
        Resposta["Mensagem"] = "Aluno não encontrado."
        Resposta["Dados"] = ''
        return jsonify(Resposta)
