import requests as Req

Url = "http://localhost/produtos/excluir/b3d304a2-b6ee-11e8-bddf-005056c00008"

Retorno = Req.api.delete(Url).json()
print(Retorno)