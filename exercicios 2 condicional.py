import os
os.system ('cls')
compras=float(input('digite o valor comprado:'))
desconto=compras*0.10
descontopro=compras*0.20
valor_desconto_normal=compras-desconto
valor_desconto_pro=compras-descontopro
if compras>=500:
    print(f'suas compras deram {valor_desconto_pro} elas tivram um desconto de 20% pos voce gastou mais de 500 reais na loja')

elif compras>=100:
    print(f'suas compras deram {valor_desconto_normal} elas tivram um desconto de 10% pos voce gastou mais de 100 reais na loja')

else:
    print (f'suas compras deram {compras} sem desconto')
