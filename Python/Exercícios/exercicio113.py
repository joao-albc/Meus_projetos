def leiaInt():
    try:
        n = int(input("Digite um valor: "))
    except Exception as erro:
        print(f'\33[0;31mERRO {erro.__class__} \033[m')
    else:
        print (f"O valor digitado foi {n}")
    finally:
        print ('Final do programa')

def leiaFloat():
    try:
        n = float(input("Digite um valor: "))
    except Exception as erro:
        print(f'\33[0;31mERRO {erro.__class__} \033[m')
    else:
        print (f"O valor digitado foi {n}")
    finally:
        print ('Final do programa')

# Programa principal
leiaInt()
leiaFloat()