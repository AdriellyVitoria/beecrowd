#ler tres valores float
a, b, c = str (input ()).split()

#classificação das variaveis:
a = float (a)
b = float (b)
c = float (c)

#verifica se os valores forma um triangulo:
triangulo = a + b > c and b + c > a and c + a > b

#se forma um triangulo, faça o perimetro dele
soma = a + b + c
if triangulo:
  print (f'Perimetro = {soma:.1f}')

# se for falso calcular a area do trapezio (soma das bases vezes a altura dividido por 2) a e b são as bases e c a altura
else:
  formula = (a + b) * c / 2
  print (f'Area = {formula:.1f}')

