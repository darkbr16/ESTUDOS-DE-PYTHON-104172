import os
os.system('cls')

vetor_livros=[]

for i in range (5):
    livro=input('digite o nome de um livro:')

    vetor_livros.append(livro)



for indice, livro in enumerate (vetor_livros,start=1):
        print(f'{indice}º: {livro}')