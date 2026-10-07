import os
os.system('cls')
contador = 0
soma_pares = 0
soma_impares = 0
qd_pares = 0
qd_impares = 0
soma_geral = 0

while True:
    valor = int(input('Digite algum número (para encerrar, digite 0): '))

    # 1. Verifica encerramento antes de somar ou contar o zero
    if valor == 0:
        break

    # 2. Atualiza os dados gerais
    contador += 1
    soma_geral += valor

    # 3. Classificação Par ou Ímpar
    if valor % 2 == 0:
        qd_pares += 1
        soma_pares += valor
    else:
        qd_impares += 1
        soma_impares += valor

# 4. Cálculos das médias (apenas no final e com proteção contra divisão por zero)
media_geral = soma_geral / contador if contador > 0 else 0
media_pares = soma_pares / qd_pares if qd_pares > 0 else 0
media_impares = soma_impares / qd_impares if qd_impares > 0 else 0

# 5. Exibição dos resultados
print('\n===== RESULTADOS =====')
print(f'Quantidade de valores ímpares:{qd_impares:.2f}')
print(f'Quantidade de valores pares:{qd_pares:.2f}')
print(f'Média dos números ímpares:{media_impares:.2f}')
print(f'Média dos números pares: {media_pares:.2f}')
print(f'Média geral dos números: {media_geral:.2f}')