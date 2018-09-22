import requests as Req

Url = "http://127.0.0.1:8080/alunos/atualizar"


Aluno = {"Nome":"YYYYY", "Ativo":False,"RA":1701169}

Retorno = Req.api.put(Url, json=Aluno).json()
print(Retorno)