import os
os.system('cls')
compras=float(input('digite o valor das compras:'))

desconto1=compras*0.10
desconto2=compras*0.15
desconto3=compras*0.20
valorfinal1=compras-desconto1
valorfinal2=compras-desconto2
valorfinal3=compras-desconto3
if compras<100:
    valor=(f'suas compras deram {compras:.2f} sem desconto ')
elif compras>=100 and compras <=200:
    valor=(f'suas compras deram {valorfinal1:.2f} tendo um desconto de 10% {desconto1:.2f} reais ')
elif compras >=200 and compras <=500:
    valor=(f'suas compras deram {valorfinal2:.2f} tendo um desconto de 15% {desconto2:.2f} reais ')
else:
    valor=(f'suas compras deram {valorfinal3:.2f} tendo um desconto de 20% {desconto3:.2f} reais ')
print(valor)