import os
import time

soma = 0
contador = 0

while True:
    os.system('cls')
    print('=====MENU=====\n')
    print('codigo|descriçao')
    print('   1  |adicionar uma nota')
    print('   2  |exibir resultado')
    codigo = input('digite um codigo: ')

    if codigo == '1':
        # --- TRAVA PARA NOTA ZERO OU NEGATIVA ---
        while True:
            nota = float(input('digite uma nota (maior que 0): '))
            if nota > 0:
                break  # Nota válida! Sai do loop de validação
            print('Erro! A nota não pode ser zero nem negativa. Tente novamente.')

        soma += nota       # Soma a nota digitada
        contador += 1     # Incrementa a quantidade de notas
        
        print('Nota adicionada com sucesso!')
        time.sleep(1)

    elif codigo == '2':
        os.system('cls')
        print('=====RESULTADO=====')
        if contador > 0:
            media = soma / contador
            print(f'Total de notas digitadas: {contador}')
            print(f'Sua média foi: {media:.2f}')
        else:
            print('Nenhuma nota foi cadastrada.')
        break

    else:
        print('Opção inválida!')
        time.sleep(1)