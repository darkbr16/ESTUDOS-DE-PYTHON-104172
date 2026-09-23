import os
os.system('cls')
soma=0
for i in range (5):
    numero=int (input(f'digite {i+1}º numero:'))

    soma=numero+soma

print(f'a soma e {soma}')