def area():
    print (f'{"-"*5}Cadastro de terreno{"-"*5}')
    lan = int(input('Largura em m²: '))
    com = int(input('Comprimento em m²: '))
    metragem = lan * com
    print (f'Um terreno com dimensões de um {lan} x {com} tem um total de {metragem}m²')

area()