import os

os.system('cls')

print('bem-vindo ao meu mercado\n')
print('código |  fruta   | preço')
print('  1    |  maçã    | R$ 7,99')
print('  2    |  banana  | R$ 9,90')
print('  3    |  uva     | R$ 14,99')
print('  4    | melancia | R$ 22,90')
print('  5    | laranja  | R$ 8,99\n')

total_compra = 0.0

while True:
    codigo = input('Digite o código correspondente à fruta: ')

    match codigo:
        case '1':
            print('Maçã adicionada (R$ 7,99).')
            total_compra += 7.99
        case '2':
            print('Banana adicionada (R$ 9,90).')
            total_compra += 9.90
        case '3':
            print('Uva adicionada (R$ 14,99).')
            total_compra += 14.99
        case '4':
            print('Melancia adicionada (R$ 22,90).')
            total_compra += 22.90
        case '5':
            print('Laranja adicionada (R$ 8,99).')
            total_compra += 8.99
        case _:
            print('Código inválido! Digite apenas um número de 1 a 5.\n')
            continue

    questionamento = input('Deseja mais alguma coisa? (sim/nao): ').strip().lower()
    
    if questionamento != 'sim':
        break
    

print(f'\nOk! O valor total da sua compra é: R$ {total_compra:.2f}')
print('Obrigado pela preferência!')