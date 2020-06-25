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
    num = (f'{num:.2f}')
    res = (f'R$ {num}')
    return res.replace(".",",")

#Exercício 109: Inserir um parâmetro extra para verificar se queremos que o número retorne com R$ ou não
#Exercício 110: Adicionar uma função resumo()

def resumo(num, aumento, reducao):
    return (f"""
    Valor analisado:\t\t{monetario(num)}
    Com o aumento de {aumento}%:\t{aumentar(num, aumento, True)}
    Com a redução de {reducao}%\t{diminuir(num, reducao, True)}
    O dobro de {num} é:\t\t{dobro(num, True)}
    A metade de {num} é\t\t{metade(num, True)}
    """)

