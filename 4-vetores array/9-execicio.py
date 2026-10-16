import os

os.system('cls')
vetor_pratos = []
vetor_preços = []

print('bem-vindo ao meu mercado\n')
print('código |   pratos   | preço')
print('  1    |  picanha   | R$ 25,00')
print('  2    |  lasanha   | R$ 20,00')
print('  3    | strogonoff | R$ 18,00')
print('  4    |   bife     | R$ 15,00')
print('  5    | pao com ovo| R$ 5,00\n')

while True:
    codigo = input('Digite o código correspondente ao prato: ').strip()

    match codigo:
        case '1':
            prato = 'picanha'
            preço = 25.0
            print('picanha adicionada (R$ 25,00).')
        case '2':
            prato = 'lasanha'
            preço = 20.0
            print('lasanha adicionada (R$ 20,00).')
        case '3':
            prato = 'strogonoff'
            preço = 18.0
            print('strogonoff adicionado (R$ 18,00).')
        case '4':
            prato = 'bife'
            preço = 15.0
            print('bife adicionado (R$ 15,00).')
        case '5':
            prato = 'pao com ovo'
            preço = 5.0
            print('pao com ovo adicionado (R$ 5,00).')
        case _:
            print('Código inválido! Digite apenas um número de 1 a 5.\n')
            continue

    # Adiciona ao carrinho após confirmação do código
    vetor_pratos.append(prato)
    vetor_preços.append(preço)

    questionamento = input('Deseja mais alguma coisa? (sim/nao): ').strip().lower()
    if questionamento != 'sim':
        break

if sum(vetor_preços) == 0:
    print('\nNenhum prato selecionado')
else:
    print('\n=PRATOS ESCOLHIDOS=')
    for i, prato in enumerate(vetor_pratos, start=1):
        print(f'{i}º prato: {prato}')

print(f'\ntotal: R$ {sum(vetor_preços):.2f}')