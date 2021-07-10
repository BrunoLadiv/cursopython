def calculadora():
    n1 = input('Numero 1: ')
    tipo = input('Operador? ')
    n2 = input('Numero 2: ')

    if n1.isnumeric() and n2.isnumeric():
        if tipo == "+":
            resultado = int(n1) + int(n2)
            print(resultado)
        elif tipo == "*":
            resultado = int(n1)* int(n2)
            print(resultado)
        elif tipo == "/":
            resultado = int(n1) / int(n2)
            print(resultado)
        elif tipo == "-":
            resultado = int(n1) - int(n2)
            print(resultado)
    else:
         print('digite um operador valido')


calculadora()



