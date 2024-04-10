from pessoa import Pessoa

aluno1 = Pessoa('Jansey', 18, 1.72, '0000000000')
aluno2 = Pessoa('Andrey', 21, 1.72, '0000000001')

class Escola:
    def __init__(self, alunos:list):
        self.alunos = alunos
      
    def addAlunos(self,aluno):
        return self.alunos.append(aluno)
      
    def removerAlunos(self,cpf):
        for aluno in self.alunos:
            if cpf == aluno['cpf']:
                self.alunos.remove(aluno)

listaAlunos = []
infinity = Escola(listaAlunos)
infinity.addAlunos(aluno1.__dict__)
infinity.addAlunos(aluno2.__dict__)
print(infinity.__dict__)
infinity.removerAlunos("0000000001")
print(infinity.__dict__)
