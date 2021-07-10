'''numero = input('Descubra se o numero é par ou impar, digite um numero inteiro:  ')


if numero.isdigit():
        numero = int(numero)
        if numero % 2 == 0: #sobra divisao por 2 = 0 numero par
                print('Numero é par')
        else:
                print('numero é impar')


else:
        print('digite um numero valido')'''


#horario = input('Digite um horário (0-23): ')
#
# if horario.isdigit():
#     horario = int(horario)
#
#     if horario < 0 or horario > 23:
#         print("Horário deve estar entre 0 e 23")
#     else:
#         if horario <= 11:
#             print('Boa dia!')
#         elif horario <= 17:
#             print('Boa tarde!')
#         else:
#             print('Boa noite!')
# else:
#     print("Por favor, digite um horário entre 0 e 23.")

# nome = input('Digite seu nome: ')
# tamanho = len(nome)
#
# if tamanho <= 4:
#     print('Seu nome é curto.')
# elif tamanho <= 6:
#     print('Seu nome é normal.')
# else:
#     print('Seu nome é muito grande.')