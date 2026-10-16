import os
os.system('cls')
import time
vetor_numero=[]
quantidade=5
for i in range(quantidade):
    ('adicionando numeros')

    numero=int(input(f'digite seu {i+1}º numero '))
    print('numero adicionado' )
    time.sleep(1)
    os.system('cls')
    if numero<0:
        numero=0
        vetor_numero.append(numero)
        print('valor negativo foi transformado em 0')
        time.sleep(2)
        os.system('cls')
    else:
        vetor_numero.append(numero)

print('==RESULTADOS==')

print(vetor_numero)