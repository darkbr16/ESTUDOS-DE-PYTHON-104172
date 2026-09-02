import os
os.system ('cls')
peso=float(input('digite seu peso:'))
altura=float(input('digite sua altura:'))

indice=peso/(altura*altura)

if indice > 40:
    resultado=('sua condiçao e obesidade grau 3 ')
elif indice >=35.0 and indice <39.9:
    resultado=('sua condiçao e obesidade grau 2')
elif indice >=30.0 and indice <34.9:
    resultado=('sua condiçao e obesidade grau 1')
elif indice >=25.0 and indice < 29.9:
    resultado=('sua condiçao e levemente acima do peso')
elif indice >=18.6 and indice < 24.9:
    resultado=('sua condiçao e peso ideal(parabens)')
else:
    resultado=('sua condiçao e abaixo do peso')
print('\n=====RESULTADO=====')
print(resultado)
