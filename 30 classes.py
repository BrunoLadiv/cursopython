
class Pessoa: #classes
    def __init__(self, nome, idade, comendo=False, falando=False): # funcoes dentro de classes = metodos
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def comer(self, alimento):

        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return
        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f{self.nome} nao esta comendo)
p1 = Pessoa('Luiz',20,)
p2 = Pessoa('Joao',40,)

p1.comer("Kibe")
p2.comer('Toba')