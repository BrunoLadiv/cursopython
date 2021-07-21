# zip - unindo iteraveis
# zip_longest - itertools

# cidades = ["Sao Paulo", "Belo Horizonte", "Salvador"]
# estados = ["SP", 'MG', 'BA']
#
# cidades_estados = zip(estados, cidades)
# print(list(cidades_estados))



list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]
#        soma y + i        # extrai os itens da lista em y e i
duas = ([y + i for y, i in zip(list1,list2)])
print(duas)


# duas = zip(list1,list2)
# for y, i in duas:
#     print(y + i),
#
# print(duas)