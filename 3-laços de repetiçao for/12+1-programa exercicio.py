import os
os.system('cls')
import time
usuario_correto='pedro'
senha_correta='12345'
tentativas=0
while True:
    usuario_digitado=input('digite seu usuario:')
    senha_digitada=(input('digite sua senha:'))
    if usuario_digitado==usuario_correto and senha_digitada==senha_correta:
        print('bem vindo pedro')
        break
    else:
        tentativas+=1
        print('senha ou usuario incorreto digite novamente')
        time.sleep(2)
        os.system('cls')
    if tentativas >=3:
        print ('voce atingio o maximo de tentativas volte mais tarde')
        time.sleep(5)
        os.system('cls')
        