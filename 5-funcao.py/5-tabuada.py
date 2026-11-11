import os
os.system("cls")

def mostrar_tabuada(numero):
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')

print ("= Solicitando dados=")
numero=int(input("digite um numero para a tabuada:"))

print("\n = Exibindo Dados =")
mostrar_tabuada(numero)