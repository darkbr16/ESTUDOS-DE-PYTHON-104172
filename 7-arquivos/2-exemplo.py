from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class clientes:
    nome:str
    idade:int
    altura:float
QUANTIDADE_CLIENTES=2
lista_cliente=[]

#satanas

#Lendo arquivo
#'r'=read
arquivo='dados_clientes.csv'
with open(arquivo,'r') as arquivo_clientes:
    for linha in arquivo_clientes:
        nome,idade,altura=linha.strip().split(',')
        lista_cliente.append(clientes(
            nome=nome,
            idade=int(idade),
            altura=float(altura)
        ))
print('\nExibindo dados dos clientes:')
for cliente in lista_cliente:
    print(f'Nome:{cliente.nome}')
    print(f'Idade:{cliente.idade}')
    print(f'Altura:{cliente.altura}')
    print('===========================')