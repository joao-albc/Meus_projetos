#Aprimorar o exercício 93

cadastros = []
cadastro = {}

while True:
    cadastro.clear
    gols_marcados = list()
    
    cadastro['nome'] = {str(input('Nome do jogador(a): '))}
    cadastro['partidas'] =  int(input(f'Quantas partidas {(cadastro["nome"])} jogou? '))
    for c in range(1,cadastro['partidas'] + 1):
        valor = int(input(f'Quantos gols na partidas {(c)}? '))
        gols_marcados.append(valor)
    print ('-='*10)

    cadastro['gols'] = gols_marcados
    cadastro['total'] = sum(gols_marcados)

    cadastros.append(cadastro.copy())
    gols_marcados.clear

    #Validação do CONTINUAR
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
        if continuar not in 'NnSs':
            print('Por favor, digitar S ou N.') 
        elif continuar in 'Ss':
            print()
            print (f'{"="*4}Novo Cadastro{"="*4}')
            print()
            break
        if continuar in 'Nn':
            break
    if continuar in 'Nn':
        print (f'{"="*4}Cadastro Finalizado{"="*4}')
        print()
        break

#Enumerate para a lista e .items para acessar os dicionários
print ('Sobre qual deles vocês deseja saber mais?')
print ()
print (f'cod{" "*6}nome{" "*10}gols{" "*6}total')
print(f'{"-"*30}')
for i, v in enumerate (cadastros):
    print (f'{i}{" "*6}{v["nome"]}{" "*6}{v["gols"]}{" "*6}{v["total"]}')


'''
    for k,v in i.items():
        if k == "nome":
            print (f'Digite {i[0]} para saber de print {v}')
'''
'''
Estava com dificuldade para fazer a divisão, por isso explicitei
print (f'Índice {i[0]}')
print (f'Chave {k}')
print (f'Valor {v}')
'''