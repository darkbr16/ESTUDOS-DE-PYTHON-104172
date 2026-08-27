import os
os.system ('cls')
idade=int(input('digite sua idade:'))

if idade<=12:
    print ('voce e crianças voce paga 20 reais (meia-entrada)')
elif idade>=65:
    print('voce e idoso paga 20 reais (meia-entrada)')
else:
    print ("voce e adulto paga 40 reias")
