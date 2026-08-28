import os
os.system ('cls')

numero1= float (input('digite o primeiro numero'))
numero2= float (input('digite o segundo numero'))
numero3=float (input('digite o terceiro numero:'))
numero4=float (input('digite o quarto numero:'))

maior= max(numero1,numero2,numero3,numero4)
menor= min(numero1,numero2,numero3,numero4)

print (f'o maior numero e {maior} e o menor e {menor}')