import os
lista_nome=[]
lista_sobrenome=[]
while True:
    os.system('cls')
    print('''== HOSPITAL CURA ==
    1-cadastro
    2-Listar pacientes
    3-Atualizar paciente
    4-Excluir paciente
    0-Sair''')

    opcao=int(input('escolha uma opçao:'))

    match opcao:
        case 1:
            print('\n == CADASTRO DO PACIENTE ==')
            nome=input('digite o primeiro nome do paciente:')
            sobrenome=input("digite o sobrenome do paciente:")
            if nome=="" or sobrenome=="":
                print("nome ou sobrenome invalidos")
            elif nome in lista_nome and sobrenome in lista_sobrenome:
                print("nome ou sobrenome ja existente")
            else:
                lista_nome.append(nome)
                lista_sobrenome.append(sobrenome)
                print('paciente cadastrado')
        case 2:
            print('\n == LISTA PACIENTES ==')
            if lista_nome ==0 and lista_sobrenome==0:
                print('nao a pacientes cadastrados')
            else:
                for i in range(len(lista_nome)):
                    print(f'- {lista_nome[i]} {lista_sobrenome[i]}')
            print(f'total de pacientes {len(lista_nome)}')
        case 3:
            print('\n == ATUALIZAR PACIENTE ==')
            nome = input("qual e o nome do paciente a ser atualizado?: ")
            sobrenome = input("qual e o sobrenome do paciente a ser atualizado?: ")
            pacientes = list(zip(lista_nome, lista_sobrenome))
            if (nome, sobrenome) in pacientes:
                i = pacientes.index((nome, sobrenome)) # Pega o índice exato do par
                lista_nome[i] = input('digite o novo nome: ')
                lista_sobrenome[i] = input('digite o novo sobrenome: ')
                print('Nome e sobrenome alterados com sucesso!')
            else:
                print('Paciente não encontrado.')
        case 4:
            print('\n == EXCLUIR PACIENTE ==')
            nome=input("qual e o nome do paciente a ser deletado?:")
            sobrenome=input("qual e o sobrenome do paciente a ser deletado?:")
            if nome in lista_nome and sobrenome in lista_sobrenome:
                i = lista_nome.index(nome)
                j = lista_sobrenome.index(sobrenome)
                if i == j: 
                    del lista_nome[i]
                    del lista_sobrenome[j]
                    print('paciente deletado com sucesso')
                else:
                    print('Paciente não encontrado.')
        case 0:
            print('adeus')
            break
        case _:
            print('opçao invalida tente novamente')
    input('pressione enter para continuar')