# listas em python fatiamento
# append, insert, pop, del, clear, extend, min, max, range


# lista = ['A', 'B', 'C', 'D', 'E', 'F']
# #         0    1    2    3    4    5
#
# print(lista[0:3])


# user = []
# passw = []
#
#
# user = user.append(input('Login: ' ))
# passw = passw.append(input('Senha ' ))
#
# print(user, passw)

#criar listas
# lista1 = list(range(0,100,7))
# print(lista1)

#jogo forca

psecreta = 'bicicleta'
digitadas = []

while True:
    letra = input('digite uma letra: ')
    if len(letra) > 1:
        print('Apenas uma letra')
        continue
    digitadas.append(letra)
    if letra in psecreta:
        print('A letra existe na palavra secreta')
    else:
        print('A Letra nao existe')
        digitadas.pop()
    secretotemp = ''
    for letrasecreta in psecreta:
        if letrasecreta in digitadas:
            secretotemp += letrasecreta
            print(letrasecreta)
        else:
            secretotemp += '*'
    print(secretotemp)

