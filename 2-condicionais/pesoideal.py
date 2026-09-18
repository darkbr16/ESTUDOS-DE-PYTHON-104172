import os
os.system ('cls')
sexo=input('voce e homem (H) ou mulher (M):').upper
altura=float(input('digite sua altura:'))
formula=(62.1*altura)-44.7
formula=(72.7*altura)-58
match sexo:
    case 'H':
        formula=(72.7*altura)-58
    case 'M':
        formula=(62.1*altura)-44.7
print(f'seu peso ideal e {formula:.2f}')