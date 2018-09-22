from server import App
from Models.resposta import Resposta
from flask import jsonify


@App.errorhandler(500)
def Trata500(error):
    Resposta["Status"] = "Não Encontrado"
    Resposta["Mensagem"] = f"Ação não executada por {error}"
    Resposta["Dados"] = ''
    return jsonify(Resposta)


@App.errorhandler(404)
def Trata404(error):
    Resposta["Status"] = "Não Encontrado"
    Resposta["Mensagem"] = "Ação não executada"
    Resposta["Dados"] = ''
    return jsonify(Resposta)
