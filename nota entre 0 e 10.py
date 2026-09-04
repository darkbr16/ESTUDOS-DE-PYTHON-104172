import os
os.system ('cls')
nota=float(input('digite sua nota:'))
notamax=10
notamin=0
if nota>=notamin and nota <=notamax:
    resultado=(f'sua nota {nota} esta entre 0 e 10')
else:
    resultado=(f'sua0, nota {nota} e invalida ela tem que esta entre 0 e 10')
print(resultado)
    
