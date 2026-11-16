import os
os.system("cls")
from datetime import date
ano_atual = date.today().year

def calculando_idade(ano):
    calculo=ano_atual-ano
    return calculo

print("Solcitando Dados")

nome=input("digite seu nome:")
ano=int(input("digite o ano do seu nascimento:"))

idade=calculando_idade(ano)

print("Mostrando Dados")

print(f"seu nome e {nome} sua idade e {idade}")
