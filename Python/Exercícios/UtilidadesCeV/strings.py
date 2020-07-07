def caixa_linha(msg):
    try:
        f = (len(msg)+4)*'~'
        return f'{f}\n {msg} \n{f}'
    except:
        return ('~'*15)

def linha(v):
    v = ("~"*v)
    return v
