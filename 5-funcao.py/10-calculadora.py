import os
os.system("cls")

def soma_numeros(numero1, numero2):
    return numero1+numero2
def subtracao_numeros(numero1, numero2):
    return numero1-numero2
def divisao_numeros(numero1, numero2):
    if numero2==0:
        return'atençao divisao por 0!'
    return numero1/numero2
def multiplicacao_numeros(numero1, numero2):
    return numero1*numero2



print("\n = Solicitando Dados =")
numero1=float(input('digite o seu primeiro numero:'))
numero2=float(input('digite o seu segundo numero:'))

soma=soma_numeros(numero1,numero2)
subratrair=subtracao_numeros(numero1,numero2)
dividir=divisao_numeros(numero1,numero2)
multiplicar=multiplicacao_numeros(numero1,numero2)

print('\n= Exibindo Dados =')
print(f'a soma dos numeros e:{soma}')
print(f'a subtraçao dos numeros e:{subratrair}')
print(f'a multiplicaçao dos numeros e:{multiplicar}')
print(f'a divisao dos numeros e:{dividir:.2f}')