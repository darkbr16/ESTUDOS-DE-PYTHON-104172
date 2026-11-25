from dataclasses import dataclass
import os

os.system("cls")

@dataclass
class Paciente:  # Maiúscula para não conflitar com a variável do loop
    nome: str
    idade: int
    telefone: str
    endereco: str

    def mostrar_dados(self):
        print(f'nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'telefone: {self.telefone}')
        print(f'endereço: {self.endereco}')

    def ligar_paciente(self):
        print(f"nome: {self.nome} | numero: {self.telefone}")

    def idade_paciente(self):
        print(f'nome: {self.nome} | idade: {self.idade}')


lista_paciente = []
print("\nSolicitando Dados")

for i in range(1):
    dados_paciente = Paciente(
        nome=input('digite seu nome: '),
        idade=int(input('digite sua idade: ')),
        telefone=input("digite seu telefone: "),
        endereco=input('digite seu endereço: ')
    )
    lista_paciente.append(dados_paciente)
    input('aperte enter para continuar')
    os.system('cls')

print("\nExibindo Dados")
for p in lista_paciente:
    p.mostrar_dados()

print('\nNumero do paciente')
for p in lista_paciente:
    p.ligar_paciente()

print('\nIdade do paciente')
for p in lista_paciente:
    p.idade_paciente()