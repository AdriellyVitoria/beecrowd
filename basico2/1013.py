#Definir a str que contém três valores.
a, b, c = str (input ()).split()

#classificando as variaveis 
a = int (a)
b = int (b)
c = int (c)
 
#apresentar o maio dos três valores
#formula para calcula maior entre a e b
ab = (a + b + abs (a - b)) /2

#formula para calcula maio entre ab e c
maior_xc = (ab + c + abs (ab - c)) / 2

#saida com resultando (eh o maior)
print (f'{maior_xc:.0f} eh o maior')
