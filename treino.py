import os
os.system ('cls')
temperatura=float(input('digite a temperatura em celsius'))

if temperatura <15:
    dizer =('esta muito frio use um agasalho')
elif temperatura >= 15 and temperatura <= 24:
    dizer =('clima agradavel')
elif temperatura >=25 and temperatura <=34:
    dizer =('esta calor beba bastante agua')
else:
    dizer=('esta muito calor evite o sol')
print (dizer)