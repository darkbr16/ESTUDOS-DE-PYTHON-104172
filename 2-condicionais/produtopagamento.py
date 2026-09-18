import os
os.system ('cls')
produto=float(input('quanto foi o valor do produto:'))
formadepagamento=input('qual serai a forma de pagamento a vista (v) ou a prazo (p):')
desconto=produto*0.10
valorfinal=produto-desconto

match formadepagamento:
    case'v':
        print(f'o valor por ser a vista ganhara 10% de desconto sendo o valor final de {valorfinal:.2f} ')
    case'p':
        parcela=int (input('quantas parcelas voce gostaria de fazer podemos parcelas de ate 6x sem juros: '))
        prestaçoes=produto/parcela
    case _:
        print('forma de pagamento invalida')
        exit()
match parcela:
    case 2:
        print(f'seram 2 parcelas de {prestaçoes:.2f}')
    case 3:
        print(f'seram 3 parcelas de {prestaçoes:.2f}')
    case 4:
        print(f'seram 4 parcelas de {prestaçoes:.2f}')
    case 5:
        print(f'seram 5 parcelas de {prestaçoes:.2f}')
    case 6:
        print(f'seram 6 parcelas de {prestaçoes:.2f}')
    case _:
        print('quantidade de parcelas invalidas')