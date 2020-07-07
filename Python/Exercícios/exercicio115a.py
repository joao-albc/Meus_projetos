from UtilidadesCeV import strings
from UtilidadesCeV import dado
def menu ():
    print (strings.caixa_linha("MENU PRINCIPAL"))
    print ("\033[32m1\033[34m Ver pessoas cadastradas:\033[m")
    print ('\033[32m2\033[34m Cadastrar nova pessoa:\033[m')
    print ('\033[32m3\033[34m Sair do sistema:\033[m')


'''
opcao = int(input(f'\033[32mSua opção: '))
print (strings.caixa_linha("Menu Principal"))
print (menu)
'''

menu()
print (strings.linha(18))
opcao = dado.leiaOpcao('\033[32mSua opção:\033[m ')
print (strings.caixa_linha(opcao))