import os
os.system ('cls')
nota1=float(input('digite sua primeira nota:'))
nota2=float(input('digite segunda  nota:'))
nota3=float(input('digite terceira nota:'))

media=(nota1+nota2+nota3)/3
if media>=7:
    resultado=('parabens voce foi aprovado')
else:
    resultado=('infelizmente voce reprovou')
print(f'media:{media}')
print(f'resultado:{resultado}')