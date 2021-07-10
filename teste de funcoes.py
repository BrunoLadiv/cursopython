# def saudacao(ola,nome):
#     print(ola," ",nome)
#
# saudacao("hey", "Bruno")


# def soma(n1,n2,n3):
#     resultado = n1 + n2 + n3
#     print(resultado)
#
#
# soma(10,5,3)

# def percentual(valor,percentual):
#     print(valor + (valor * percentual / 100))
# percentual(100,25)
# percentual(10,5)


#ftest

def fizzbuzz(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return "FizzBuzz"
    elif n1 % 5 == 0:
        return "Buzz"
    elif n1 % 3 == 0:
        return "Fizz"
    else:
        return n1

resultado = fizzbuzz(4)

print(resultado)


