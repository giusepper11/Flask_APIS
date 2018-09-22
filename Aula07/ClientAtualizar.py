import requests as Req

Url = "http://localhost/produtos/atualizar"
Produto = {"Id":"b3d304a2-b6ee-11e8-bddf-005056c00008", "Nome":"TV 50 pol.", "Preco":2499}

Retorno = Req.api.put(Url, json=Produto).json()
print(Retorno)