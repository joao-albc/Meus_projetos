import inimigos
jogador = {}

def cadastrar_jogador():
    nome = str(input('Esolha o seu nome:'))
    return nome

'''
print ('\n========Nova batalha======')
print ('Seja bem-vindo ao jogo de luta básico')
print ('Insira os seus dados')
'''

jogador["Nome"] = cadastrar_jogador()
print (jogador)
