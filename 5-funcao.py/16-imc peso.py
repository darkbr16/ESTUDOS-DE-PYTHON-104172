import os
os.system('cls')
def calculadora_imc(peso, altura):
    return peso / (altura ** 2)

def tabela_De_peso(imc):
    if imc < 18.5:
        classificacao = "Abaixo do peso"
        recomendacao = "Consulte um nutricionista para orientação"
    elif imc >= 18.5 and imc <= 24.9:
        classificacao = "Peso normal"
        recomendacao = "Mantenha hábitos saudáveis!"
    elif imc >= 25 and imc <= 29.9:
        classificacao = "Sobrepeso"
        recomendacao = "Considere uma dieta balanceada e atividade física"
    elif imc >= 30 and imc <= 34.9:
        classificacao = "Obesidade grau 1"
        recomendacao = "Procure orientação de um profissional de saúde"
    elif imc >= 35 and imc <= 39.9:
        classificacao = "Obesidade grau 2"
        recomendacao = "Consulte um médico para avaliação e orientação"
    else:
        classificacao = "Obesidade grau 3"
        recomendacao = "Busque assistência médica imediatamente"
    return classificacao, recomendacao

print('\n= Solicitando Dados =')
peso = float(input('Digite seu peso (kg): ').replace(',', '.'))
altura = float(input('Digite sua altura em metros (ex: 1.70): ').replace(',', '.'))

imc = calculadora_imc(peso, altura)
classificacao, recomendacao = tabela_De_peso(imc)

print('\n= Exibindo Resultados =')
print(f'Peso: {peso} kg')
print(f'Altura: {altura}')
print(f'IMC: {imc:.2f}')
print(f'Classificação: {classificacao}')
print(f'Recomendação: {recomendacao}')