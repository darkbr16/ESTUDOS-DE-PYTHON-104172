import os
import time

login_salvo = 'pedro'
senha_salva = '12345'  # Salvamos como string para bater com o input()
tentativas = 0
limite_tentativas = 3

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Se exceder o limite, bloqueia o acesso
    if tentativas >= limite_tentativas:
        print('Número máximo de tentativas excedido!')
        print('Tente novamente mais tarde.')
        time.sleep(5)
        break

    print(f'Tentativa {tentativas + 1} de {limite_tentativas}')
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if login == login_salvo and senha == senha_salva:
        print('\nBem-vindo!')
        break
    else:
        tentativas += 1
        print('\nLogin ou senha inválidos.')
        print('Tente novamente...\n')
        time.sleep(2)