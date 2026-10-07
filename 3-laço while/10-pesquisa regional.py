import os
os.system('cls')
qd_mulher=0
soma_salarios=0
total_pessoas=0
maior_idade=18
menor_idade=1000
mulheres_supersalarios=0
while True:
    print('=====MENU=====')
    print('CODIGO|DESCRIÇAO')
    print('  1   |adicionar pessoa')
    print('  2   |exibir resultados')
    print('  3   |sair')
    resposta=input('digite o codigo correspondente:')

    if resposta=='1':
        total_pessoas+=1
        idade=int(input('digite sua idade:'))
        sexo=input('digite seu sexo M para homem F para mulher:').upper()
        salario=float(input('qual e seu salario:'))
        soma_salarios+=salario
        os.system('cls')
        if sexo=='M':
            break
        elif sexo=='F':
            qd_mulher+=1
            if idade>maior_idade:
                maior_idade=idade
            if idade<menor_idade:
                menor_idade=idade
            if sexo=='f' and salario>=5000:
                mulheres_supersalarios+=1
                os.system('cls')
        
    
    if resposta=='2':
        os.system('cls')
        if mulheres_supersalarios>0:
            media=soma_salarios/qd_mulher
            print('\n=====RESULTADOS=====')
            print(f'media salarial:{media}')
            print(f'maior idade:{maior_idade}')
            print(f'menor idade:{menor_idade}')
            print(f'menor idade:{menor_idade}')
            print(f'mulheres como salario acima de 5 mil {mulheres_supersalarios}')
    else:
        break