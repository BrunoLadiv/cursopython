class Pessoa:                                 #
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nameclass = self.__class__.__name__


class Aluno(Pessoa):
        def estudar(self):
            print(f'{self.nameclass} estudando' )

class Professor(Pessoa):
    def ano(self):
        print(f'{self.nameclass} falando' )

class AlunoVip(Aluno):
    def rico(self):
        print('tratamento especial')
    def estudar(self):
        print('Nao Precisa Estudar')

p1 = Professor('Marcos', 30)

a1 = AlunoVip("Jonas",15)
a2 = Aluno('Mario',20)
print(p1.nome)
p1.ano()

print(a1.nome)
a1.rico()
a1.estudar()
print('***************************')
print(a2.nome)
a2.estudar()
