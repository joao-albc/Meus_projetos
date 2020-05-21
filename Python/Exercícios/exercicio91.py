import random
import time
import operator
jogo = {
	'jogador 1': random.randint(1,6),
	'jogador 2': random.randint(1,6),
	'jogador 3': random.randint(1,6),
	'jogador 4': random.randint(1,6)
	}
raking = list()
print ('Valores sorteados')
for k, v in jogo.items():
    time.sleep(1)
    print (f'O {k} tirou o valor {v} no dado')
ranking = sorted(jogo.items(), key = operator.itemgetter(1), reverse = True)
print('-='*15)
print('== Ranking dos Jogadores==')
for i,v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    ##time.sleep(1)



'''
#O exercício que eu fiz (incompleto)

jogador = {}
ranking = []
for c in range(1,5):
    valor = random.randint(1,7)
    print('processando...')
    time.sleep(1)
    print(f"jogador{(c)} tirou {valor}")
    jogador['posiçao'] = (f'jogador{(c)}')
    jogador['valor'] = (valor)
    ranking.append(jogador.copy())
    jogador.clear
print (ranking)
'''