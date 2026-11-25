from dataclasses import dataclass
import os

os.system('cls')

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str
    def mostrar_Dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'Email: {self.email}')
        print('=' * 15)
    
    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print('=' * 15)
    
    def zap_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print('=' * 15)

    

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
    cliente.mostrar_Dados()
print("\nExibindo email marketing")
for cliente in lista_cliente:
    cliente.email_marketing()
print("\nExibindo zap marketing")
for cliente in lista_cliente:
    cliente.zap_marketing()