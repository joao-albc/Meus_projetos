import inimigos
jogador = {}
inimigo = {}

def cadastrar_jogador():
    nome = str(input('Esolha o seu nome: '))
    jogador['nome'] = nome

def resto():
    print(f'Qual caminho você {jogador["nome"]}, deseja tomar?')
    print('1: Esquerda \n2: Direita')
    caminho = int(input('\nDigite sua escolha: '))

    if (caminho == 1):
        print (f'Você acabou de encontrar com {inimigos.inimigo[(caminho)-1]["nome"]}')
    elif (caminho == 2):
        print (f'Você acabou de encontrar com {inimigos.inimigo[(caminho)-1]["nome"]}')
    #inimigo 

#def titulos():

print ('\n========Nova batalha======')
print ('Seja bem-vindo ao jogo de luta básico')
print ('Insira os seus dados')
print ()

cadastrar_jogador()
resto()
#inimigo_ativo = ini