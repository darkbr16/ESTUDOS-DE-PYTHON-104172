from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    #variavel:tipo da variavel
    nome:str
    idade:int
    altura:float
    peso:float
lista_clientes=[]
print('\nSolicitando dados de dois Clientes')
for i in range(2):
    dados_do_cliente=Cliente(
        nome=input('\ndigite seu nome:'),
        idade=int(input('digite sua idade:')),
        altura=float(input("digite sua altura:")),
        peso=float(input("digite seu peso:")))
    
    lista_clientes.append(dados_do_cliente)
os.system("cls")
print("Exibindo Dados")
for cliente in lista_clientes:
    print(f'Nome:{cliente.nome}')
    print(f"Idade:{cliente.idade}")
    print(f'altura:{cliente.altura}')
    print(f"peso:{cliente.peso}")
    print('='*15)