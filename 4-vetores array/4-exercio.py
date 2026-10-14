import os
os.system('cls')

vetor_notas=[]
quantidade=4

for i in range (quantidade):
    nota=float(input(f'digita a {i+1}º nota:'))
    vetor_notas.append(nota)
media=sum(vetor_notas)/quantidade

print('\n =EXIBINDO AS NOTAS=')
if media>=7:
    print ('aprovado')
elif media<=6 and media>=5:
    print('recuperaçao')
else:
    print('reprovado')
maior_nota=max(vetor_notas)
menor_nota=min(vetor_notas)

for posicao,nota in enumerate(vetor_notas,start=1):
    print(f'{posicao}º nota: {nota}')
print(f'sua media foi {media}')
print(f'maior nota: {maior_nota}')
print(f'menor nota: {menor_nota}')