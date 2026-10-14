import os
os.system('cls')

vetor_notas=[]
quantidade=3

for i in range (quantidade):
    nota=float(input(f'digita a {i+1}º nota:'))
    vetor_notas.append(nota)
media=sum(vetor_notas)/quantidade

print('\n =EXIBINDO AS NOTAS=')

for posicao,nota in enumerate(vetor_notas,start=1):
    print(f'{posicao}º nota: {nota}')
print(f'sua media foi {media}')