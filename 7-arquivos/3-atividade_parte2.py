from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class fornecedores:
    nome:str
    email:str
    telefone:str
    enderoco:str
QUANTIDADE_FORNECEDORES=3
lista_fornecedores=[]
#ladrao

arquivo='dados_fornecedor.csv'
with open (arquivo,'r') as arquivo_fornecedor:
    for linha in arquivo_fornecedor:
        nome,email,telefone,enderoco=linha.strip().split(',')
        lista_fornecedores.append(fornecedores(
            nome=nome,
            email=email,
            telefone=telefone,
            enderoco=enderoco
        ))
print('\nExibindo Dados do Cliente:')
for fornecedor in lista_fornecedores:
    print(f'Nome:{fornecedor.nome}')
    print(f'Email:{fornecedor.email}')
    print(f'Telefone:{fornecedor.telefone}')
    print(f'Enderoço:{fornecedor.enderoco}')
