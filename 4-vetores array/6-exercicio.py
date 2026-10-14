import os
os.system('cls')

vetor_impares=[]
vetor_pares=[]
quantidade_pares=0
quantidade_impares=0

QUANTIDADE=6
for i in range (QUANTIDADE):
        numero=int(input('digite um numero:'))
        if numero % 2==0:
            quantidade_pares+=1
            vetor_pares.append(numero)
        else:
            quantidade_impares+=1
            vetor_impares.append(numero)

print(f'quantidade de impares {quantidade_impares}')
print(vetor_impares)
print(f'quantidade de pares {quantidade_pares} ')
print(vetor_pares)