from Models.alunos import Alunos


def ConsultarAluno(RA):
    for a in Alunos:
        if str(a["RA"]) == RA:
            return True, a
    return False, None
