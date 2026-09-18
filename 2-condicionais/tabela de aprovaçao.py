import os
os.system('cls')
nome=input('digite seu nome:')
nota1=float(input('diga sua primeira nota:'))
nota2=float(input('diga sua segunda nota:'))

media=(nota1+nota2)/2

if media >= 9: 
    resultado=('o aluno foi aprovado com nota A')
elif media >=7.5 and media < 9:
    resultado=('o aluno foi aprovado com nota B')
elif media >= 6 and media < 7.5:
    resultado=('o aluno foi aprovado com nota C')
elif media >=4 and media <6:    
    resultado=('o aluno foi reprovado com nota D')
else:
    resultado=('foi reprovado nota E')

print ('o aluno {} que tirou as notas {} e {} teve a media de {} {} '.format(nome,nota1,nota2,media,resultado))