import os
os.system ('cls')

macas=int(input('quantas maças voce quer:'))

if macas <12:
    custo=macas*1.30
else:
    custo=macas*1

print(f'valor total da compra e de {custo:.2f} reais')

