cores = (
    '\033[m',       #0 -- sem cores
    '\033[0:30:41m', #1 -- vermelho
    '\033[0:30:41m', #2 -- verde
    '\033[0:30:42m', #3 -- amarelo
    '\033[0:30:43m', #4 -- azul
    '\033[0:30:44m', #5 -- roxo
    '\033[7:30m'    #6 -- branco
);

def título(texto):
    print (cores[1], end = ' ')
    texto = print('SISTEMA DE AJUDA PYTHON')
    print (cores[0], end = ' ')

def fun_ou_bibl():
    from time import sleep
    while True:
        ajuda = input('Digite sua busca: ')
        print (f'Localizando o comando {ajuda}...')
        sleep(0.7)
        help(ajuda)
        if ajuda == "sair":
            break

#fun_ou_bibl()
título('Teste')
        
