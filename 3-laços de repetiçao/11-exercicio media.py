import os
os.system ('cls')
QUANTIDADE_DE_NOTAS=4
nota=0

for i in range (QUANTIDADE_DE_NOTAS):
    nota+=float (input(f'digite {i+1}º nota:'))
    media=nota/QUANTIDADE_DE_NOTAS
print(f'a media e {media}')