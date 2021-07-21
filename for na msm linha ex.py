lista1 =[10,5,15,20]
lista2 =[10,5,15,20]



for y, i in zip(lista1 , lista2):
    resultado = y + i
    print((resultado))

resultado = [y+i for y,i in zip(lista1, lista2)]
print(resultado)