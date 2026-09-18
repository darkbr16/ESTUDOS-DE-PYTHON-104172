import os 
os.system('cls')

numero1=int(input('digite um numero:'))
numero2=int(input('digite outro numero:'))

media=(numero1 +numero2)/2
soma=numero1+numero2
multiplicaçao=numero1*numero2

if numero1 > numero2:
    resultado= ('o numero {} e maior que o numero {}'.format(numero1,numero2))

elif numero1 == numero2:
    resultado=('o numero {} e igual ao numero {}'.format(numero1,numero2))

else:
    resultado=('o numero {} e maior que o numero {}'.format(numero2,numero1))

print ('=====RESULTADOS=====')
print('a media entre {} e {} da {}'.format(numero1,numero2,media))
print('a soma entre {} e {} o resultado e {}'.format(numero1,numero2,soma))
print('a multiplicaçao entre {} e {} o resultado e {}'.format(numero1,numero2,multiplicaçao))
print(resultado)