# == > >= <= !=

print('Banco HAHA')
print('****************')

escolha = input('Precisa de um emprestimo?  responda com "sim" ou "nao" ')

if escolha == 'sim':
    idade = input('Qual sua idade? ')

    if int(idade) >= 18:
        concedido = input('Qual a quantia desejada? ')
        print(f'o emprestimo de {concedido} foi concedido')
    else: print('tenha uma boa tarde')
else: print('tenha uma boa tarde')