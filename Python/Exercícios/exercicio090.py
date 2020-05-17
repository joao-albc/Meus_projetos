aluno = dict()
all = []
status = ['Aprovado', 'Recuperação']
for c in range (0,3):
##while True:
    aluno['Nome'] = str(input('Nome aluno: '))
    aluno['Média']= int(input(f"A média de {aluno['Nome']} é: "))
    if aluno['Média'] < 6:
        print (f"{aluno['Nome']} está de recuperação")
    else:
        print('Aprovado(a)')
    print ()
    '''all.append(aluno.copy())
for a in all:
    for n, m in a.items():
        print (f'{n} teve média {m}')'''
