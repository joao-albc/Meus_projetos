#Funções do exercício 107
def aumentar(num, porc):
    f = num+(num * (porc/100))
    return f

def diminuir(num, porc):
    f = num - (num * (porc/100))
    return f

def dobro(num):
    f = num * 2
    return f

def metade(num):
    f = num / 2
    return f
        
#Função adicionada pelo exercício 108
'''
def monetario(num):
    num = (f'{num:.2f}')
    res = (f'R$ {num}')
    return res.replace(".",",")
'''

#Exercício 109: Inserir um parâmetro extra para verificar se queremos que o número retorne com R$ ou não
#Exercício 110: Adicionar uma função resumo()

def resumo(num, aumento, reducao):
    return (f"""
    Valor analisado:\t\tR$ {(num):.2f}
    Com o aumento de {aumento}%:\tR$ {aumentar(num, aumento):.2f}
    Com a redução de {reducao}%:\tR$ {diminuir(num, reducao):.2f}
    O dobro de {num} é:\t\tR$ {dobro(num):.2f}
    A metade de {num} é\t\tR$ {metade(num):.2f}
    """)

#print (resumo(10,5,8))