import os
os.system("cls")

def conversao_centimetros(metros):
    return metros*100

print("\n= Exibindo Dados =")
metros=float(input('digite uma medida em metros para converter:'))


converter=conversao_centimetros(metros)

print("\n = Exibir Dados =")
print(f"a conversao de {metros} para centimetros e {converter}")