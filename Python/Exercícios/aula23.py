try:
    a = int(input('Qual a sua idade: '))
    b = int(input('Multiplicar por: '))
    m = a * b
except Exception as erro:
    print(f'Infelizmente tivemos um problema por {erro.__class__}')
else:
    print(f'A multiplicação entre {a} e {b} resultam em {m}')
finally:
    print (f'Fim da aplicatção')