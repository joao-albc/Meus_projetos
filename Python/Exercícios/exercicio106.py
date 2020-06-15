def fun_ou_bibl():
    from time import sleep
    while True:
        print('SISTEMA DE AJUDA PYTHON')
        ajuda = input('Digite sua busca: ')
        print (f'Localizando o comando {ajuda}...')
        sleep(0.7)
        help(ajuda)
        if ajuda == "sair":
            break

fun_ou_bibl()
        
