import os
os.system('cls')
import time
tentativas=0
print("faça um cadastro\n")
cadastro=input('digite seu username:')
senha=int(input('digite sua senha:'))
os.system('cls')

while True:
    tentativas+=1
    print('faça o seu login')
    login_digitado=input('digite seu username:')
    senha_digitada=int(input('digite sua senha:'))
    if login_digitado==cadastro and senha==senha_digitada:
        print(f'bem vindo {cadastro}')
        break
    if tentativas>=3:
        os.system('cls')
        print('limite de tentativas atigindo tente novamente mais tarde')
        break
    else:
        print('username ou senha errados')
        time.sleep(2)
        os.system('cls')
