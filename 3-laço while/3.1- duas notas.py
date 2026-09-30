import os
os.system('cls')

media=0
for i in range (2):
    nota=float(input(f'digite{i+1}º sua nota:'))
    media=(media+nota)
while True:
    if nota <0 or nota>10:
        print('nota invalida')
    else:
        print(f'sua media e {media}')
        break