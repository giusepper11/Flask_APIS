from Models.alunos import Alunos


def ExcluirAluno(RA):
    for a in Alunos:
        if str(a['RA']) == RA:
            Alunos.remove(a)
            return True, Alunos
    return False, None
