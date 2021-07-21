#funcao decoradora
from time import time
from time import sleep

def master(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A funcao{funcao.__name__} levou {tempo} ms para executar')
    return interna

@master
def demora():
    for i in range(5):
        sleep(1)

demora()

# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
