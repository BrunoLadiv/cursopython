''' print('Calculadora de Soma')
n1 = input('numero 1?')
n2 = input('Numero 2?')

if n1.isdecimal() and n2.isdecimal():
    n1 = int(n1)
    n2 = int(n2)
    resultado = n1 + n2
    print('O Resultado e:', resultado)
else:
    print('Coloque um numero valido') '''

print('Calculadora de Soma')
n1 = input('numero 1?')
n2 = input('Numero 2?')

try:
    n1 = int(n1)
    n2 = int(n2)
    resultado = n1 + n2
    print('O Resultado e:', resultado)
except:
    print('Coloque um numero valido')