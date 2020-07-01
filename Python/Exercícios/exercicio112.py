from UtilidadesCeV import moeda
#A função moeda está sendo puxada de uma pasta dentro do pacote UtilidadesCeV, diferentemente do que acontecia no exercício 110
from UtilidadesCeV import dado
import strings
from random import randint

'''
valor = randint(1,10)
print (f'Valor: {valor}')
'''
#Valores aleatórios


escolha = dado.leiaDinheiro("Digite um valor: ")
valor = escolha
aumento = randint(1,100)
#print (f'Aumento: {aumento}%')
reduzir = randint(1,100)
#print (f'Redução: {reduzir}%')


print (strings.caixa_linha('Resumo de valor'))
print (moeda.resumo(valor,aumento, reduzir))

