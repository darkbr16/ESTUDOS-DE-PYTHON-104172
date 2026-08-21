import os
os.system('cls')

print('=solicitando dados=')
valor=float(input('digite o valor:'))
desconto=valor*0.10
valor_com_desconto=valor-desconto

print('\n=exibindo dados=')
print('o valor com desconto de 10%:',valor_com_desconto)
