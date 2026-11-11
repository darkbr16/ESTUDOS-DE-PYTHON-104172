import os
os.system("cls")

lista_produtos = []

def mostrar_dados(lista_produtos):
    for i in range(len(lista_produtos)):
        print(f'{i + 1}º Produto: {lista_produtos[i]}')
def cadastro_dados(produto):
    for i in range(3):
        produto = input(f"Digite o nome do {i + 1}º produto: ")
        lista_produtos.append(produto)

print("= Solicitando Dados =")
cadastro_dados(lista_produtos)
print("\n= Exibindo Dados =")
mostrar_dados(lista_produtos)