import os
os.system('cls')

dia = input('Digite um dia da semana: ').strip().lower()

match dia:
    case "segunda":
        print('Hoje é segunda-feira')
    case "terça" | "terca":
        print('Hoje é terça-feira')
    case "quarta":
        print('Hoje é quarta-feira')
    case "quinta":
        print('Hoje é quinta-feira')
    case "sexta":
        print('Hoje é sexta-feira')
    case "sabado" | "sábado" | "domingo":
        print('Hoje é final de semana')
    case _:
        print('Dia inválido')
print('===FIM===')