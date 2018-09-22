from Models.alunos import Alunos

def AtualizarAluno(Dados):
    for a in Alunos:
        if a['RA'] == Dados['RA']:
            a["Nome"] = Dados["Nome"]
            a["Ativo"] = Dados["Ativo"]
            return True, a
    return False, None
