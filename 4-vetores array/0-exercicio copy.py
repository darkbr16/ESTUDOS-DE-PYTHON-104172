import os
os.system('cls')

print('=INSERINDO NUMEROS NO VETOR=')
vetor_numeros=[]

numero= int(input('digite seu numero:'))
vetor_numeros.append(numero)
numero= int(input('digite seu numero:'))
vetor_numeros.append(numero)
numero= int(input('digite seu numero:'))
vetor_numeros.append(numero)



print('\n= EXIBINDO NUMEROS DO VETOR =')

print(f'primeira posiçao do vetor: {vetor_numeros[0]}')
print(f'ultima posiçao do vetor: {vetor_numeros[2]}')