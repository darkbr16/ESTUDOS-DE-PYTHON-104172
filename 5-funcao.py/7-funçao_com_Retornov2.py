import os
os.system("cls")
#funçao com retorno
def calcular_notas(nota1, nota2):
    resultado=(nota1 + nota2)/2
    return resultado

print('= Solicitando Notas =')
nota1=float(input('Digite a primeira nota:'))
nota2=float(input('Digite a segunda nota:'))
#usando a funçao com parametros e com return e inserido o return sempre dentro de uma variavel 'soma'
media=calcular_notas(nota1, nota2)

print('= Exibindo Notas =')
print(f'media:{media}')