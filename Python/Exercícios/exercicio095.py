#Aprimorar o exercício 93

cadastros = []
cadastro = {}
gols_marcados = list()
while True:
    cadastro.clear
    
    cadastro['nome'] = {str(input('Nome do jogador(a): '))}
    cadastro['partidas'] =  int(input(f'Quantas partidas {(cadastro["nome"])} jogou? '))


    for c in range(1,cadastro['partidas'] + 1):
        valor = int(input(f'Quantos gols na partidas {(c)}? '))
        gols_marcados.append(valor)
    print ('-='*10)

    cadastro['gols'] = gols_marcados
    #ARRUMAR OS GOLS MARCADOS
    cadastro['total'] = sum(gols_marcados)

    cadastros.append(cadastro.copy())
    gols_marcados.clear
    #Continuar? Sim ou Não é preciso corrigir essa parte
    
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
        break
print (cadastros)

''''
print (cadastro)
print ('-='*10)

for k,v in cadastro.items():
    print(f'O campo {k} recebeu o valor {v}')

print ('-='*10)

print(f'O jogador(a) {cadastro["nome"]} jogou {cadastro["partidas"]}')

for k, v in enumerate (gols_marcados):
     print(f'Na partida {k}, fez {v} gols')'''