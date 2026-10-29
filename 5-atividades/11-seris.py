import os
os.system("cls")
series_lista = []
print("""===SÉRIES===

1- Cadastrar série
2- Listar séries
0- Sair""")

while True:
    opcao = int(input("Digite a opção desejada: "))
    os.system("cls")

    match opcao:
        case 1:
            print("==cadastrar series==")
            serie = input("Digite o nome da série: ")
            if serie=='':
                print("escreva uma série válida!")
            elif serie in series_lista:
                print("série já cadastrada!")                   
            else:
                series_lista.append(serie)
                print("série adicionada com sucesso!")
        case 2:
            if len(series_lista)==0:
                print("Não há séries cadastradas!")
            else:
                print("Listar séries")
                for i, serie in enumerate(series_lista, start=1):
                    print(f"{i}º série: {serie}")
                print('total de séries cadastradas: ', len(series_lista))
            
        case 0:
            print("adeus")
            break
        case _:
            print("Opção inválida!")