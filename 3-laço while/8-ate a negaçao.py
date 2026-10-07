import os
os.system('cls')
import time
contador=0
soma=0
while True:
    valor=int(input('digite um valor:'))
    if valor <0:
        media=soma/contador
        print ('o resultado chegou ao negativo')
        print(media)
        break
    else:
        contador+=1
        soma+=valor
