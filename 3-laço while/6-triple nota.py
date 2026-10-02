import os
os.system('cls')
import time
soma=0
quantidade_de_notas=3

for i in range (quantidade_de_notas):

    while True:
        nota=float(input(f'digite a {i+1}º sua nota entre 0 e 10:'))
        if nota>=0 and nota<=10:
            soma=soma+nota
            break
        else:
            print()
            print('nota invalida,tente novamente!')
            time.sleep(2)
            os.system('cls')

media=soma/quantidade_de_notas
if media
print(f'sua media foi {media}')

