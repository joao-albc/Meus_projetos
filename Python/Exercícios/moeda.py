#Funções do exercício 107
def aumentar(num, porc, mon=False):
    f = num+(num * (porc/100))
    if mon == True:
        return monetario(f)
    else:
        return f

def diminuir(num, porc, mon=False):
    f = num - (num * (porc/100))
    if mon == True:
        return monetario(f)
    else:
        return f

def dobro(num, mon=False):
    f = num * 2
    if mon == True:
        return monetario(f)
    else:
        return f

def metade(num, mon=False):
    f = num / 2
    if mon == True:
        return monetario(f)
    else:
        return f
        
#Função adicionada pelo exercício 108
def monetario(num):
    num = float(num)
    res = (f'R$ {num}')
    return res

#Exercício 109: Inserir um parâmetrom extra para verificar se queremos que o número retorne com R$ ou não