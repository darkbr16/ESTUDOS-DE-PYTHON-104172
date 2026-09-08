import os
os.system ('cls')
sexo=input('digite seu sexo:')
idade=int (input('digite sua idade:'))

if sexo=='masculino' and idade >= 18:
    serviço=('voce precisa servir ao exercito')
else:
    serviço=('voce nao precisa servir ao exercito')
print(serviço)