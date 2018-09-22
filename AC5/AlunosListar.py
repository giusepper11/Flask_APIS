import requests as Req

Url = "http://127.0.0.1:8080/alunos"

Retorno = Req.api.get(Url).json()
print(Retorno)