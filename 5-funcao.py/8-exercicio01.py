import os
os.system("cls")

def calculos_pares(numero):
    if numero % 2==0:
        resultado=(f'{numero} e par')
    else:
        resultado=(f'{numero} e impar ')
    return resultado
print("=Solicitando Dados=")
numero=int(input("digite um numero:"))

resultado=calculos_pares(numero)

os.system("cls")
print("\n=Exibindo Resultados=")
print(resultado)