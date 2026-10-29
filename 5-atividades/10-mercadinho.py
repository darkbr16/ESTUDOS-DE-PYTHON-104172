import os
os.system("cls")
import time
produtos = []


while True:
    print("""===MERCADINHO DENDEZEIROS===
    1-cadastrar produto
    2-listar produtos
    0-sair""")
    opcao = int(input("Digite a opção desejada: "))
    os.system("cls") #limpa a tela
    match opcao:
        case 1:
            print("==Cadastrar produto==")
            produto = input("Digite o nome do produto: ")
            if produto=='':
                print("escreva um produto válido!")
                time.sleep(1.5)
                os.system("cls") #limpa a tela
                
            elif produto in produtos:
                print("produto já cadastrado!")
                time.sleep(1.5)
                os.system("cls") #limpa a tela
            else:
                produtos.append(produto)
                print("produto adicionado com sucesso!")
                time.sleep(1.5)
                os.system("cls") #limpa a tela
            
        case 2:
            if len(produtos)==0:
                print("Não há produtos cadastrados!")
                time.sleep(1.5)
                os.system("cls") #limpa a tela
                
            else:
                print("Listar produtos")
                for i, produto in enumerate(produtos, start=1):
                    print(f"{i}º produto: {produto}")
                print('total de produtos cadastrados: ', len(produtos))
                #len() é uma função que retorna o tamanho de uma lista
            time.sleep(1.5)
            continua=input("Digite enter para continuar...")
            os.system("cls") #limpa a tela
        case 0:
            print("ate mais")
            break
        case _:
            print("Opção inválida!")
            time.sleep(1.5)
            os.system("cls") #limpa a tela