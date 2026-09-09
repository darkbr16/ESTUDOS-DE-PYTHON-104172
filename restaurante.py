import os
os.system("cls")
print ('=====BEM VINDO AO RESTAURANTE======')

print('os pratos disponives no cardapio sao')
print('codigo     prato      valor   ')
print('  1       picanha     25.00$  ')
print('  2       lasanha     20.00$  ')
print('  3      strogonoff   18.00$  ')
print('  4    bife acebolado 25.00$  ')
print('  5     pão com ovo    5.00$  ')


codigo=int(input('digite um dos codigos no cardapio para solicitar os pratos:'))

match codigo:
    case 1:
        print('otima escolha prepararemos sua picanha o valor e ')
    case 2:
        print('bela escolha prepararemos sua lasanha')
    case 3:
        print('boa escolha prepararemos seu strogonoff')
    case 4:
        print('maravilhosa escolha prepararemos seu bife acebolado')
    case 5:
        print('ok prepararemos seu pao com ovo')
