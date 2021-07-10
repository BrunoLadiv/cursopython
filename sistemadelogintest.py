login = []
passw = []


while True:
    registro = input('Registre um login com no maximo 6 Caracteres ')
    if len(registro) > 6:
        print('Maximo de 6 Caracteres')
        continue
    else:
        login.append(registro)
    senha = input('Registre sua senha min 6 caracteres:' )
    if len(senha) < 6:
            print('Minimo 6 Caracteres')
    else:
        passw.append(senha)
        break
print('Conta Registrada! ')
logar = input('Deseja Logar? ')
if logar == 'sim':
        login1 = input('Seu login: ')
        senha1 = input('Sua Senha: ')
        if login1 in login and senha1 in passw:
            print('Voce foi logado no sistema! ')
        else:
            print('Login ou senha incorretos. ')
else:
    print('tenha um bom dia')