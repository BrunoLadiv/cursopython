# carrinho = []
#
# print('seu carrinho: TV LG: 1200R$ ********  PS5: 5000R$ *******')
# finalizar = input('Finalizar compra? ')
#
#
# if finalizar == 'sim':
#     carrinho.append(1200),
#     carrinho.append(5000),
#     print(f'Valor total: {sum(carrinho)} R$')
# else:
#     print('*******')

carrinho = []
carrinho.append(("Produto 1", 30))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 50))

total =sum([float(y) for x,y in carrinho])

print(total)