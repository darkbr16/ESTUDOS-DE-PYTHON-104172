import os

lista_nome = []
lista_posicao = []
lista_numero = []

while True:
    os.system("cls")
    print("\n== CADASTRO PSG ==")
    print("1 - Cadastrar jogador")
    print("2 - Listar jogadores")
    print("3 - Atualizar jogador")
    print("4 - Excluir jogador")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            print("\n-- Novo Jogador --")
            nome = input("Nome: ")
            posicao = input("Posição: ")
            numero = input("Número: ")

            if nome and posicao and numero:
                lista_nome.append(nome)
                lista_posicao.append(posicao)
                lista_numero.append(numero)
                print("Jogador cadastrado!")
            else:
                print("Preencha todos os campos!")

        case "2":
            print("\n-- Lista de Jogadores --")
            if not lista_nome:
                print("Nenhum jogador cadastrado.")
            else:
                for i in range(len(lista_nome)):
                    print(f"{i + 1}. {lista_nome[i]} | {lista_posicao[i]} | Camisa {lista_numero[i]}")

        case "3":
            print("\n-- Atualizar Jogador --")
            if not lista_nome:
                print("Nenhum jogador para atualizar.")
            else:
                # Mostra a lista para o usuário escolher pelo número da ordem (índice)
                for i in range(len(lista_nome)):
                    print(f"{i + 1} - {lista_nome[i]}")
                
                num = int(input("Digite o número do jogador na lista acima: ")) - 1
                
                if 0 <= num < len(lista_nome):
                    lista_nome[num] = input("Novo nome: ")
                    lista_posicao[num] = input("Nova posição: ")
                    lista_numero[num] = input("Novo número: ")
                    print("Jogador atualizado!")
                else:
                    print("Jogador inválido.")

        case "4":
            print("\n-- Excluir Jogador --")
            if not lista_nome:
                print("Nenhum jogador para excluir.")
            else:
                for i in range(len(lista_nome)):
                    print(f"{i + 1} - {lista_nome[i]}")
                
                num = int(input("Digite o número do jogador para excluir: ")) - 1
                
                if 0 <= num < len(lista_nome):
                    del lista_nome[num]
                    del lista_posicao[num]
                    del lista_numero[num]
                    print("Jogador excluído!")
                else:
                    print("Jogador inválido.")

        case "0":
            print("Saindo...")
            break

        case _:
            print("Opção inválida!")

    input("\nPressione Enter para continuar...")