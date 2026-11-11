import os
os.system("cls")
nome_lista=[]
email_lista=[]
telefone_lista=[]

def logo_senai():
    print('\n')
    print('='*15)
    print("  SENAI-BAHIA")
    print('='*15)

def mostrar_dados():
    print(f" nome {nome} ")
    print(f" email {email} ")
    print(f" telefone {telefone} ")

nome=""
email=""
telefone=""
while True:
    os.system("cls")
    logo_senai()
    print('== MENU == ')
    print('''1-adicionar usuario
2-mostrar dados
0-sair ''')

    pergunta=int (input('selecione uma das opçoes acima:'))
    os.system("cls")
    match pergunta:
        case 1:
            logo_senai()

            print("== Solicitantdo dados ==")
            nome=input("digite seu nome:")
            email=input("digite seu email:")
            telefone=input("digite seu numero:")
            
        case 2:
            if not nome:
                print("nenhum usuario cadastrado")
            else:
                logo_senai()
                print("== Exibindo Dados ==")
                mostrar_dados()
                
        case 0:
            print('ate mais!')
            break
        case _:
            print('numero nao indentificado')
    continua=input("pressione enter para continuar")








