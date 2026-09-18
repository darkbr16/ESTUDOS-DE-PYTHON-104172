import os
os.system ('cls')

numero=float(input('digite um numero para o calculo:'))


for i in range (1,11):
    print (f'{numero} + {i} = {numero+i}')
print ('subtraçao')
for i in range (1,11):
    print (f'{numero} - {i} = {numero-i}')
print ('multiplicaçao')
for i in range (1,11):
    print (f'{numero} * {i} = {numero*i}')
print ('divisao')
for i in range (1,11):
    print (f'{numero} / {i} = {numero/i}')