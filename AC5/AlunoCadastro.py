import requests as Req

Url = "http://127.0.0.1:8080/alunos/cadastrar"


Aluno = {"Nome":"XXXXX", "Ativo":True,"RA":1701168}

Retorno = Req.api.post(Url, json=Aluno).json()
print(Retorno)