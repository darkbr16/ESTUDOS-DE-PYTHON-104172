import os
os.system('cls')
print ('=====calculadora=====')
numero1=float (input ('digite um numero:'))
numero2=float (input ('digite outro numero:'))

soma=(numero1+numero2)
subtraçao=(numero1-numero2)
multiplicaçao=(numero1*numero2)
divisao=(numero1/numero2)

print ('a soma entre {} e {} o resultado {}'.format(numero1,numero2,soma))
print ('a subtração entre {} e {} o resultado {}'.format (numero1,numero2,subtraçao))
print ('a multiplicaçao entre {} e {} o resultado {}'.format(numero1,numero2,multiplicaçao))
print ('a divisao entre {} e {} o resultado {}'.format(numero1,numero2,divisao))


