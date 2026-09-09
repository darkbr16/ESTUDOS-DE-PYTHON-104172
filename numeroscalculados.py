import os
os.system ('cls')
numero1=float (input('digite um numero:'))
numero2=float (input('digite outro numero:'))
usar= input ('digite um dos caracteres para o calculo(+,-,* ou /):')

match usar:
    case "*":
        print(f'a multiplicaçao entre o numero {numero1} e o {numero2} e {numero1*numero2:.2f}')
    case "+":
        print (f' a soma entre  o numero {numero1} e o {numero2} e {numero1+numero2:.2f}')
    case "-":
        print(f'a subtraçao entre {numero1}e o {numero2} e {numero1-numero2:.2f}')
    case "/":
        print (f'a divisao entre o {numero1} e o {numero2} e {numero1/numero2:.2f}')
    case _:
        print ('resultado invalido')

