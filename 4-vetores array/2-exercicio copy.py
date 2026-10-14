import os
os.system('cls')

vetor_notas=[]
print('\n=INSERINDO  NOTAS=')
for i in range (3):
    nota=float(input('digite uma nota:'))
    vetor_notas.append(nota)
media=sum(vetor_notas)
os.system('cls')
print('\n ===NOTAS===')
for indice,nota in enumerate(vetor_notas,start=1):
    print(f'{indice}º: {nota}')

print(f'soma:{media}')