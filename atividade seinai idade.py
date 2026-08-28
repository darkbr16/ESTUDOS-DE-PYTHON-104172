import os
os.system ('cls')

idade=int(input('digite sua idade:'))

if idade < 16:
    voto=('nao pode vota')
elif idade< 18:
    voto=('voto opicional')
elif idade >= 65:
    voto=('voto opicional')
else:
    voto=('VOTO OBRIGATORIO')

print("-" * 30)
print(f"RESULTADO: {voto.title()}")
print("-" * 30)