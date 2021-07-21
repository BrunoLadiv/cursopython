

print('********** ORGANIZADOR DE TAREFAS ********** ')





while True:
            print('Oque deseja Fazer? ')
            print('Adicionar tarefa [1]')
            print('Desfazer [2]')
            print('Listar tarefas [3]')
            print('Sair [4] ')
            a1 = input('Ecolha opcao de [1] a [4]: ')
            if a1.isdecimal():
                a1 = int(a1)
                if a1>0 and a1<5:
                    if a1 == 1:
                        with open('lista.txt', 'a+') as file:

                            file.write(input("Oque deseja Adicionar? : "))
                            file.write(' ')
                            print("Adicionado a lista!")
                            print("*******************")

                            a1 = 0

                    elif a1 ==2:
                        lines= []
                        with open('lista.txt', 'w+') as file:

                            for line in file:
                                lines.append(line.strip())
                                file.write(lines)
                        a1=0



                    elif a1 ==3:
                        with open('lista.txt', 'r') as file:
                            listaemtexto = file.read()
                            print(listaemtexto)

                            a1=0

else:
    print('Invalido, Escolha uma opcao de [1] a [4]')