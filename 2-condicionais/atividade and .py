import os
os.system('cls')

login = input('digite o seu nome de usuario: ').strip()
senha = input('digite sua senha: ').strip()

loginsalvo = 'pedro henrique'
senhasalva = '123'

if login == loginsalvo and senha == senhasalva:
    resolva = 'seja bem-vindo pedro'
else:
    resolva = 'login ou senha invalidos'

print(resolva)