def linha_pontilhada():
    print (f'{"-"*30}')

def ficha(nome=0,gols=0):
    nome = str(input('Nome do jogador? '))
    gols = str(input('Quantidade de gols? '))
    if nome == '':
        nome = 'desconhecido'
    if gols == '':
        gols = 'zero'
    linha_pontilhada()
    print (f'O jogador(a) {nome} fez {gols} gol(s) no campeonato')
    linha_pontilhada()


ficha()
#print (f'O jogador(a) {nome} fez {gols} gol(s) no campeonato')

'''
Código do Professor Guanabara

def ficha(jog='<desconhecido>', gol=0):
	print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
m = str(input("Nom do Jogador: "))
g = str(input("Número de Gols: "))
if g.isnumeric():
	g = int(g)
else:
	g = 0
if n.strip() =='':
	ficha(gol=g)
else:
	ficha(n,g)
'''