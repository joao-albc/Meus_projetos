from datetime import date 

hoje = date.today().year

pessoa = {}

while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['nascimento'] = int(input('Ano de nascimento: '))
    pessoa['ctps'] = int(input('Nº da carteira de trabalho: '))
    if pessoa['ctps'] == 0:
        break
    pessoa['salario'] = int(input('Salário'))
    pessoa['idade'] = hoje - (pessoa['nascimento']) 

print (pessoa)
