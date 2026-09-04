import os
os.system ('cls')

media=float(input('digite sua media:'))
faltas=int(input('digite quantas vezes voce faltou:'))
limitemedia=7
limitefalta=40
if media <limitemedia and faltas>limitefalta:
    resultado=('voce reprovou')
else:
    resultado=('voce foi aprovado')
print(resultado)