from Models.alunos import Alunos


def Cadastrar(dados):
    RA = dados['RA']
    Nome = dados['Nome']
    Ativo = dados['Ativo']
    for a in Alunos:
        if RA == a['RA']:
            return False, None
    Alunos.append({"RA": RA, "Nome": Nome, "Ativo": Ativo})
    return True, Alunos
