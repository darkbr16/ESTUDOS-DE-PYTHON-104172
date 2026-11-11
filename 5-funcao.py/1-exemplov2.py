import os
os.system('cls')

#funçao.
def cabecalho():
    print('\n')
    print('='*15)
    print("  SENAI BAHIA")
    print('='*15)
    

#usando cabeçalo
cabecalho()
nome=input("digite seu nome:")

#usando cabeçalo
cabecalho()
idade= int(input("digite sua idade:"))


#usando cabeçalo
cabecalho()
print(f'nome:{nome}')
print(f'idade:{idade}')