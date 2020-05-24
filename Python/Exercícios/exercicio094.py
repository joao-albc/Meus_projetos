cadastros = {}

while True:
    cadastros['nome'] = str(input('Nome: '))
    while True:
        cadastros['Gênero'] = str(input('Gênero: [M/F] '))
        if cadastros['Gênero'] not in "FfMm":
            print('Por favor, digite apenas M ou F')
        else:
            break
   
    cadastros['Idade'] = int(input(f'Idade de {cadastros["nome"]}: '))
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in "Nn":
        break