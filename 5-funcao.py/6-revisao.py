import os
os.system('cls')
#funçao e uma pasta que guarda e pode guardar codigos para serem deslocados
def logo_senai():
    os.system('cls')
    print('='*15)
    print("     SENAI")
    print('='*15)
logo_senai()

def mostrar_dados(nome, idade):
    print(f"{nome} tem {idade} anos ")
    

print('= Solicitando dados =')
nome=input('Digite seu nome:')
idade= int (input('Digite sua idade:'))

logo_senai()

print('\n Exibindo Dados =')

mostrar_dados(nome, idade)