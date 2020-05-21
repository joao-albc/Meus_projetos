cadastro = {}

nome = {str(input('Nome do jogador(a): '))}
partidas =  int(input(f'Quantas partidas {nome} jogou?'))
gols =  {}
gols_marcados = []
for c in range(1,partidas + 1):
    valor = int(input(f'Quantos gols na partidas {(c)}? '))
    gols_marcados.append(valor)
print ('-='*10)
gols = gols_marcados
#print (gols)
total = {'total':sum(gols_marcados)}
#print (total)
cadastro['nome'] = nome
cadastro['gols'] = gols_marcados
cadastro['total'] = total

print (cadastro)