import os
os.system('cls')
import time

def calcular_notas(lista_notas):
    return sum (lista_notas)/ len(lista_notas)

def mostrar_notas(lista_notas):
    print('\n= Exibindo Notas =')
    for nota in lista_notas:
        print(f'nota:{nota}')
def status_do_aluno(media):
    if media>=7:
        resultado='aprovado'
    else:
        resultado='reprovado'
    return resultado

lista_notas=[]

print("= Solicitando Notas =")
for i in range (2):
    while True:
        nota=float(input('Digite uma nota:'))
        if nota>= 0 and nota<=10:
            lista_notas.append(nota)
            break
        else:
            print('nota invalida , tente novamente! \n')
            time.sleep(1)
            os.system('cls')
media=calcular_notas(lista_notas)
status_aluno=status_do_aluno(media)

os.system('cls')
print('\n= Exibindo Resultados =')
mostrar_notas(lista_notas)
print(f'\nMedia: {media}')
print(f'situaçao do aluno: {status_aluno}')