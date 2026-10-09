import os
os.system('cls')
import time

total_de_familias=0
maior_salario=0
menor_salario=999999990
soma_salario=0
soma_filhos=0
while True:

    print('=====MENU=====')
    print('codigo|descriçao')
    print('  1   |adicionar familia:')
    print('  2   |sair e exibir resultados:')
    resposta=input('digite o codigo que voce deseja:')
    if resposta=='1':
        total_de_familias+=1
        salario=float(input('digite a renda familiar:'))
        crianças=int(input('quantas tem a familia:'))
        print('familia adicionada')
        time.sleep(2)
        os.system('cls')
        soma_salario+=salario
        soma_filhos+=crianças
        media_salario=soma_salario/total_de_familias
        media_filhos=soma_filhos/total_de_familias
        maior_salario = max(maior_salario, salario)
        menor_salario = min(menor_salario, salario)
    else:
        print('/n=====resultado=====')
        print(f'total de familias que responderam a pesquisa {total_de_familias}')
        print (f'media salarial das familias {media_salario}')
        print (f'media de filhos  na familias {media_filhos}')
        print(f'maior salario {maior_salario}')
        print(f'menor salario {menor_salario}')