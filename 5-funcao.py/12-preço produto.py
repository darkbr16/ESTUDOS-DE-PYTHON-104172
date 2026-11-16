import os
os.system("cls")

def compra_taxa(valor):
    if valor<100:
        return valor*1.10
    elif valor>=100:
        return valor*1.20
    

print("Solicitando preço")
valor=float(input("digite quanto foi o produto:"))

taxado=compra_taxa(valor)


print('mostrando o amor')
print(f'conta sem amor R$ {valor}')
print(f'a conta com o amor R$ {taxado}')