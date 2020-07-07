#Cadastros para teste:
cadastros = [{"Nome":"João","Idade":30},{"Nome":"Thais","idade":34},{"Nome":"Ana","Idade":35}]
#cadastros = []

def mostrar_cadastros():
    for k, v in enumerate(cadastros):
        for c in v:
            print (f'{v[c]}\t',end=' ')
        print()

def cadastrar():
    válido = False
    while not válido:
        pessoa = {
            "nome":str(input('Nome: ')),
            "idade":int(input('Idade: ')),
        }
        print ()
        cadastros.append(pessoa.copy())
        pessoa.clear
        c = str(input('Deseja continuar?'))
        print ()
        if c in "Nn":
            print ()
            return True


#cadastrar()
#mostrar_cadastros()
#print (cadastros)