import os
os.system('cls')
import time

soma=0
contador=0
while True:
    nota=float(input(f'digite uma nota:'))
    soma+=nota
    contador+=1
    
    resposta=input('voce gostaria de adicionar mais uma nota digite y para sim n para nao:').upper()
    if resposta=='N':
        media=soma/contador
        print (f'sua media foi {media:.2f}')
        break
    else:
        print ('ok adicione a outra nota')
        time.sleep(1.5)
        os.system('cls')

