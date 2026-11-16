import os
os.system("cls")
vetor_notas=[]
QUANTIDADE_NOTAS=3
def calculo_media(nota):
    calculo=sum(vetor_notas)/QUANTIDADE_NOTAS
    return calculo

def notas_amostrar():
    os.system("cls")
    print('\n== Boletim == ')
    for indice in enumerate (vetor_notas,start=1):
        print(f'nota: {indice}')
    print(f'media final:{media}')

for i in range(QUANTIDADE_NOTAS):
    
    nota=float(input(f"digite sua {i+1}º nota:"))
    vetor_notas.append(nota)
    os.system('cls')

media=calculo_media(nota)
amostrador=notas_amostrar()

print (amostrador)