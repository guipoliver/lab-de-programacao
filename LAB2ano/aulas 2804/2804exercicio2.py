#criqar um cadastro de alunos com classes: aluno, curso, turma

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

class Turma:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

curso1 = Curso("Informática Básica", "INF001")

aluno1 = Aluno("Ana", "001")
aluno2 = Aluno("Bruno", "002")

curso1.adicionar_aluno(aluno1)
curso1.adicionar_aluno(aluno2)

turma1 = Turma("Turma A", curso1)

turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)

print("Alunos no curso:", curso1.nome)
for aluno in curso1.alunos:
    print(aluno.nome)

print("\nAlunos na turma:", turma1.nome)
for aluno in turma1.alunos:
    print(aluno.nome)
