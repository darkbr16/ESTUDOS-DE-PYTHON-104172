import os
os.system ('cls')
QUANTIDADE_DE_NOTAS=3
nota=0

for i in range (QUANTIDADE_DE_NOTAS):
    nota+=float (input(f'digite {i+1}º nota:'))
    media=nota/QUANTIDADE_DE_NOTAS
if media >=7:
    resultado=('parabens voce foi aprovado')
elif media>=4:
    resultado=('voce esta na recuperaçao')

else:
    resultado=('voce reprovou')

print('======BOLETIM=====')

print(f'sua media foi {media}')
print(resultado)