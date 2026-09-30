import os
os.system('cls')

soma=0
q=2

for i in range (q):

    while True:
        nota=float(input(f'digite a {i+1}º sua nota entre 0 e 10:'))
        if nota>=0 and nota<=10:
            soma=soma+nota
            break
        else:
            print()
            print('nota invalida,tente novamente!')

media=soma/q
print(f'sua media foi {media}')
