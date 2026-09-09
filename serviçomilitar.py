import os
os.system ('cls')
sexo=input('digite seu sexo (M OU F):').upper()
idade=int (input('digite sua idade:'))

if sexo=='M' and idade >= 18:
    serviço=('voce precisa servir ao exercito')
else:
    serviço=('voce nao precisa servir ao exercito')
print(serviço)
