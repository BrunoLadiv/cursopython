from data import nomes, produtos, lista

# lista = [2,4,5,6,8,3]
#
# def multiplica(r):
#     r = r * 5
#     return r
#
# novo = list(map(multiplica, lista)) #map faz passar a funcao em listas tipo um for
# for i in novo:
#     print(novo)

def filtra(pessoa):
    if pessoa['idade'] <= 18:
        return True
#nova_lista = filter(lambda x:  x > 5, lista) # filtra numeros maoires que 5 da lista
#nova_lista = filter(lambda p:  p['preco'] > 30, produtos) # filtra numeros maoires que 5 da lista
nova_lista = filter(filtra , nomes) # filtra numeros maoires que 5 da lista
for produto in nova_lista:
    print(produto)