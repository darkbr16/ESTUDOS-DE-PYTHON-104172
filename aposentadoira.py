import os
from datetime import date
os.system ('cls')
codigo=int(input('digite seu codigo'))
nome=input('digite seu nome:')
ano_de_nascimento=int(input('digite seu ano de nascimento:'))
idade=date.today().year-ano_de_nascimento
tempoclt=int(input('digite  seu tempo trabalhado:'))

if idade >=65 or tempoclt >=30:
    aposentadoria=('requer aposenta')
else:
    aposentadoria=('nao requer aposentadoria')

print(f'o empregado {nome}  {aposentadoria} ')
