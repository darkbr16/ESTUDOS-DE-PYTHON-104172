import os
os.system ('cls')
numero1=float(input('digite o primeiro numero:'))
numero2=float(input('digite o segundo numero:'))

media=(numero1+numero2)/2
soma=(numero1+numero2)
multiplicaçao=(numero1*numero2)
if numero1 > numero2:
    maior=numero1
    menor=numero2
else:
    maior=numero2
    menor=numero1
print('a soma entre {} e {} o valor e {} '.format (numero1,numero2,soma))
print('a multiplicaçao entre {} e {} o resultado e {} '.format(numero1,numero2,multiplicaçao))
print('a media entre {} e {} o resultado e {} '.format(numero1,numero2,media))
print('o maior numero e {} eo menor e {}'.format(maior,menor))
