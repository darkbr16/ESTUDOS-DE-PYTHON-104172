import os
os.system ('cls')

dia=int (input('digite um numero de (1 a 7):'))

match dia:
    case 1:
        print('domingo final de semana')
    case 2|3|4|5:
        print('dia util')
    case 7:
        print('sábado final de semana')
    case _:
        print('dia invalido')
print('===FINAL===')