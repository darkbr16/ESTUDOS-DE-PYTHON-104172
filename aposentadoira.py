import os
os.system ('cls')
nome=input('digite seu nome:')
idade=int(input('digite sua idade:'))
tempoclt=int(input('digite  seu tempo trabalhado:'))

if idade >=65 or tempoclt >=30:
    aposentadoria=('requer aposenta')
else:
    aposentadoria=('nao requer aposentadoria')

print(f'o empregado {nome}  {aposentadoria} ')