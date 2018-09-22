import requests as Req

Url = "http://127.0.0.1:8080/alunos/excluir/1701168"


Retorno = Req.api.delete(Url).json()
print(Retorno)
