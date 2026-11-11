import os


lista_prdutos=[]

while True:
    os.system("cls")
    print("""\n===MERCADINHO DENDEZEIROS===
    1-cadastar
    2-listar todos os produtos
    3-atualizar produto
    4-remover produto
    5-buscar produto
    0-sair """)

    opcao=int(input("escolha uma opção:"))
    
    match opcao:
        case 1:
            #CREATE
            print("\n== CADASTRAR PRODUTO ==")
            nome_produto=input("digite o nome do produto:").strip().upper()
            if nome_produto=='':
                print('o nome do produto deve ser inserido')
            elif nome_produto in lista_prdutos:
                print ('produto ja cadastrado')
            else:
                lista_prdutos.append(nome_produto)
                print("produto cadastrado com sucesso!")
        case 2:
            #READ
            print('\n== PRODUTOS NO ESTOQUE ===')
            for produto in lista_prdutos:
                print(f'- {produto}')
            print(f'total:{len(lista_prdutos)}')
        case 3:
            #UPDATE
            print('\n== ATUALIZAR PRODUTO ==')
            nome=input("Qual produto deseja atualizar?:").strip().upper()
            if nome in lista_prdutos:
                posicao=lista_prdutos.index(nome)
                novo=input('novo nome:')
                lista_prdutos[posicao]=novo
                print('produto alterado com sucesso!')
            else:
                print("produto nao encontrado")

        case 4:
            #DELETE
            print('\n==REMOVER PRODUTO ==')
            nome=input("Qual produto deseja remover?:").strip().upper()
            if nome in lista_prdutos:
                lista_prdutos.remove(nome)
                print('produto removido com sucesso!')
            else:
                print("produto nao encontrado")
        case 5:
            #READ EXTRA
            print('\n==ENCONTRAR PRODUTO ==')
            nome=input("Qual produto deseja buscar?:").strip().upper()
            if nome in lista_prdutos:
                print('produto encontrado com sucesso!')
            else:
                print("produto nao esta no estoque")
        case 0:
            print("saindo do programa...")
            break
        case _:
            print('opçao invalida! \nTente novamente')
    input('pressione enter pra continuar')
            