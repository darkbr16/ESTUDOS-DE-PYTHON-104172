from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class fornecedores:
    nome:str
    email:str
    telefone:str
    enderco:str
QUANTIDADE_CLIENTES=3
lista_fornecedor=[]
#destruidor de pais

print("Solicitando dados")

for i in range(QUANTIDADE_CLIENTES):
    novo_fornecedor=fornecedores(nome=input("digite seu nome:"),
                            email=input("digite seu email:"),
                            telefone=input("digite seu numero:"),
                            enderco=input("digite seu endereço:")
                            )
    lista_fornecedor.append(novo_fornecedor)

arquivo="dados_fornecedor.csv"
with open (arquivo,'a') as arquivo_de_fornecedor:
    for fornecedor in lista_fornecedor:
        arquivo_de_fornecedor.write(f'{fornecedor.nome},{fornecedor.email},{fornecedor.telefone},{fornecedor.enderco}\n')
print("fornecedor salvo!")