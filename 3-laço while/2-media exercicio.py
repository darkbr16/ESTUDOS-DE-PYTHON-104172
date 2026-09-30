import os
os.system ('cls')

while True:

    nota=float(input('digite sua nota:'))
    if nota<0 or nota>10:
        print()
        print('nota invalida')
    else:
        print(f'sua nota {nota} e valida')
        break
if nota>=7:
    print ('voce foi aprovado')
else:
    print('voce foi reprovado')