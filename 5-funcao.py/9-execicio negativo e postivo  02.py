import os
os.system("cls")

def calculo_numero(numero):
    if numero>0:
        resultado=(f"{numero} e postivo")
    
    elif numero==0:
        resultado=("0 e um numero neutro")

    else:
        resultado=(f'{numero} e negativo ')
    return resultado

print("\n= Solicitando Dados =")
numero=int(input("digite um numero:"))

resultado=calculo_numero(numero)
os.system('cls')
print('\n = Exibindo Dados =')
print(resultado)