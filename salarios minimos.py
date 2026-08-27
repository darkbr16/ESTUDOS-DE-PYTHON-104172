import os
os.system('cls')
print('=====calculadora de salarios minimos=====')
salario=float(input('digite seu salario:'))
calculo= (salario/1621)
print ('=====resultado=====')
print (f'seu salario e equivalente a {calculo:.2f} salarios minimos'.format(calculo))
