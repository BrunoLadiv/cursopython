

# def func1():
#      return "ola mundo"
#
# def func2(fucao):
#      return fucao()
#
# resultado = func2(func1)
#
# print(resultado)


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}'
def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'luiz')
executando2 = mestre(saudacao, 'luiz', saudacao='bom dia')

print(executando)
print(executando2)

