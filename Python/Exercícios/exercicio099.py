def maior(* núm):
    val_maior = 0
    for valor in núm:
        if valor > val_maior:
            val_maior = valor
    print(f'O maior número é {val_maior}')

def contador(* núm):
    for valor in núm:
        print(valor)


contador(2,5,4,3,2)
maior(2,5,4,3,2)

