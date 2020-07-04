import urllib.request
import strings

try:
    conexao = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print ('Deu erro')
else:
    print ('O site está funcionando!')
finally:
    print (strings.caixa_linha('Programa finalizado!'))