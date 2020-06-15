def notas(* num, sit = 0):
    """
    -> Função par analisar notas e situações de vários alunos.
	: param num: uma ou mais notas dos alunos (aceita várias)
	: param sit: valor opcional, indicando se deve ou não adicionar a situação
	: return: dicionário com várias informações sobre a situação da turma
    """
    maior = menor = num[0]
    média = sum(num)/len(num)
    for c in num:
        if c > maior:
            maior = c
        elif c < menor:
            menor = c
    avaliação = {'Total':len(num),'Maior nota':maior,'Menor':menor,'Média':média}
    
    if sit == True :
        if média >= 8:
            sit = "EXCELENTE"
        elif média >= 6:
            sit = "BOA"
        else:
            sit = "RUIM/PÉSSIMA"
        avaliação['situação'] = (sit)

    print (avaliação)


    '''
    >>>>RESOLUÇÃO DO PROFESSOR<<<<
    def notas (*n, sit=False):
    r=dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
    '''
#help(notas)
notas (2,4,6,7, sit = True)