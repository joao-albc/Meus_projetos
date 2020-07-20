receitas_cadastradas = []
usuarios_cadastrados = []
id_cadastrados = {}

#Ações relacionadas aos usuários

def cadastrar_usuario(): 
    novo= {
    #"Id": como realizar o id autointeger
    "Nome":str(input('Nome: ')),
    "Sobrenome":str(input('Sobrenome: ')),
    "Idade":int(input('Idade: ')),
    "Gênero":str(input('M/F/Outros')),
    #"Telefone"  receber DDD + prefixo + número
    "e-mail":str(input('E-mail:'))
    }
    #É importante que haja uma verificação se o usuário já existe
    #Acredito que isso possa ser feito através da verificação de id
    cadastro = novo.copy()
    usuarios.append(cadastro)


def deletar_usuario():
    novo = {
    "Produto":str(input('Produto')),
    "Tipo":str(input('Tipo:'))
    }
#def editar_usuario():


#Ações relacionadas às receitas
def cadastrar_receita():
    novo = {
    "Produto":str(input('Produto')),
    "Tipo":str(input('Tipo:'))
    }

'''
Principal
'''
#cadastrar_usuario()
print (novo)