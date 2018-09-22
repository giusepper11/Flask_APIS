import requests as Req

Url = "http://localhost/produtos/cadastrar"
Produto = {"Nome":"TV 50 pol.", "Preco":1999}

Retorno = Req.api.post(Url, json=Produto).json()
print(Retorno)