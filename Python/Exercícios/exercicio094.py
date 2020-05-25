cadastro = {}
soma = media = 0
cadastros = []
while True:
    cadastro.clear
    cadastro['nome'] = str(input('Nome: '))
    while True:
        #Linha 7 =-= .upper()[0] =-= comando aidionado para pegar apenas a primeira letra
        cadastro['Gênero'] = str(input('Gênero: [M/F] ')).upper()[0]
        if cadastro['Gênero'] not in "FM":
            print('Por favor, digite apenas M ou F')
        else:
            break
    cadastro['Idade'] = int(input(f'Idade de {cadastro["nome"]}: '))
    soma+= cadastro['Idade']

    # copia e limpeza do dicionário
    
    cadastros.append(cadastro.copy())    
    
    #continuidade dos cadastros
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in "Nn":
        print (f'{4*"=-"} CADASTRO FINALIZADO {4*"=-"}')
        break
    elif continuar not in "Ss":
        print ('Por favor, digite apenas S ou N')
    else:
        print (f'{4*"="}Novo cadastro{4*"="}')

for c in cadastros:
    print (c)

media = soma/len(cadastros)
print (f'A) Foram realizados {len(cadastros)} cadastros')

print (f'B) A média de idade foi {media:2.2f}')
print (f'C) As mulheres cadastradas foram' ,end='')
for p in cadastros:
    if p["Gênero"] in"Ff":
        print(f'{p["nome"]} ', end='')
print()
print (f'D) Lista de pessoas acima da média:', end='')
print()
for p in cadastros:
    if p["Idade"] >= (media):
        print('     ', end='')
        for k, v in pitems():
            print (f'{k} = {v}; ', end='')
        print()
print ('<< ENCERRADO >>')