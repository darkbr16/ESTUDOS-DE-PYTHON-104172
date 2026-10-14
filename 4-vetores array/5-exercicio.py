import os
os.system('cls')

vetor_numero=[]
QUANTIDADE=5
for i in range(QUANTIDADE):
    numero=int (input('digite um numero:'))
    vetor_numero.append(numero)
numero_max=max(vetor_numero)
numero_min=min(vetor_numero)

print (f'o maior numero:{numero_max}')
print (f'o menor numero:{numero_min}')
