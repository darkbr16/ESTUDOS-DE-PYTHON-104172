from dataclasses import dataclass
import os

os.system('cls')

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str

lista_cliente = []
print('Solicitando Dados')
for i in range(2):
    dados_cliente = Cliente(
        nome=input("Digite seu nome: "),
        telefone=input("Digite seu número de telefone: "),
        email=input("Digite seu email: ")
    )
    lista_cliente.append(dados_cliente)
    print("Cadastrado com sucesso!")
    input("Aperte Enter para continuar...")
    os.system("cls")

print("\nExibindo dados")
for cliente in lista_cliente:
    print(f'Nome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'Email: {cliente.email}')
    print('=' * 15)