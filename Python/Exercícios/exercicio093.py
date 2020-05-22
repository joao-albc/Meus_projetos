cadastro = {}

cadastro['nome'] = {str(input('Nome do jogador(a): '))}
cadastro['partidas'] =  int(input(f'Quantas partidas {(cadastro["nome"])} jogou? '))
gols_marcados = []

for c in range(1,cadastro['partidas'] + 1):
    valor = int(input(f'Quantos gols na partidas {(c)}? '))
    gols_marcados.append(valor)
print ('-='*10)

cadastro['gols'] = gols_marcados
cadastro['total'] = sum(gols_marcados)

print (cadastro)
print ('-='*10)

for k,v in cadastro.items():
    print(f'O campo {k} recebeu o valor {v}')

print ('-='*10)

print(f'O jogador(a) {cadastro["nome"]} jogou {cadastro["partidas"]}')

for k, v in enumerate (gols_marcados):
     print(f'Na partida {k}, fez {v} gols')
