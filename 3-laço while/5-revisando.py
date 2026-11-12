import os 
os.system('cls')
import time
senha_correta='1234'
tentativas=0

while True:
    tentativas += 1
    senha_digitada=input('Digite a senha: ')
    if senha_digitada==senha_correta:
        print('Acesso permitido!')
        print(f'Número de tentativas: {tentativas}')
        break
    else:
        if tentativas==3:
            print('Número máximo de tentativas atingido. Acesso negado!')
            break
        print('Senha incorreta! Tente novamente.')
        time.sleep(1)
        os.system('cls')