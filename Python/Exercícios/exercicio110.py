import moeda
import strings
from random import randint

valor = float(input('Digite um valor: '))
aumento = int(input('Qual "%" deseja aumentar:'))
reduzir = int(input('Qual "%" deseja reduzir:'))

'''

print (f'O {valor} recebeu o aumento de {aumento} e ficará em {moeda.aumentar(valor,aumento)}')
print (f'O {valor} recebeu o redução de {aumento} e ficará em {moeda.diminuir(valor,reduzir)}')
print (f'O dobro de {valor} é igual a {moeda.dobro(valor)}')
print (f'O metade de {valor} é igual a {moeda.metade(valor)}')
'''
print (strings.caixa_linha('Resumo de valor'))
print (moeda.resumo(valor,aumento, reduzir))