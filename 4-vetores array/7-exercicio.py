import os
os.system('cls')
import time
vetor_numeros=[]
quantidade=5
soma=0
quantidade_numeros_neg=0
for i in range(quantidade):
    print('adicionando numeros')
    numero=int(input('digite um numero:'))
    print('numero adicionado')
    time.sleep(1)
    os.system('cls')
    if numero>0:
        soma+=numero
    else:
        quantidade_numeros_neg+=1
        vetor_numeros.append(numero)

print('\n==RESULTADOS==')

print(f'quantidade de numeros negativos {quantidade_numeros_neg}')
print(f'numeros negativos {vetor_numeros}')
print(f'soma dos numeros prositivos {soma}')