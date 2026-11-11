import os
os.system("cls")

def logo_senai():
    print('\n')
    print('='*15)
    print("  SENAI-BAHIA")
    print('='*15)

def mostrar_dados():
    print(f"\nseu nome {nome} seu email {email} seu numero {telefone} ")

logo_senai()

print("== Solicitantdo dados ==")
nome=input("digite seu nome:")
email=input("digite seu email:")
telefone=input("digite seu numero:")
os.system("cls")

logo_senai()

print("== Exibindo Dados ==")
mostrar_dados()