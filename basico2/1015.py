#ler 4 valores, 2 em cada linha:
x1, y1 = str (input ()).split ()
x2, y2 = str (input ()).split ()

#classificando as variaveis x1 e y1
x1 = float (x1)
y1 = float (y1)
#classificando as variaveis x2 e y2
x2 = float (x2)
y2 = float (y2)

#calcular a distancia entre eles
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5

#saida do resultando:
print (f'{distancia:.4f}')
