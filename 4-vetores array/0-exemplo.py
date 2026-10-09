import os
os.system('cls')

vetor_nomes= []

for i in range (3):
    nome=input('digite seu nome:')
    vetor_nomes.append(nome) #inserindo a nota no vetor de notas

for i in range (3):
    print(f'nomes:{vetor_nomes[i]}')
