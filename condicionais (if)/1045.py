#ler tres valores float:
valor1, valor2, valor3 = str (input ()).split()

#classificação das variaveis:
valor1 = float (valor1)
valor2 = float (valor2)
valor3 = float (valor3)

#classificando valor1 como maior
if valor1 >= valor2 and valor1 >= valor3 :
  a = valor1

  if valor2 >= valor3 :
    b = valor2
    c = valor3
  else :
    b = valor3
    c = valor2

elif valor2 >= valor1 and valor2 >= valor3:
  a = valor2

  if valor1 >= valor3:
    b = valor1
    c = valor3
  else:
    b = valor3
    c = valor1

elif valor3 >= valor2 and valor3 >= valor1:
  a = valor3
  
  if valor2 >= valor1:
    b = valor2
    c = valor1
  else:
    b = valor1
    c = valor2
  

#determine o tipo de triângulo que a (o maior lado), b e c formam:
if a >= b + c:
  print ('NAO FORMA TRIANGULO')

else:

  if a ** 2 == b ** 2 + c ** 2:
    print ('TRIANGULO RETANGULO')
  elif a ** 2 > b ** 2 + c ** 2:
    print ('TRIANGULO OBTUSANGULO')
  elif a ** 2 < b ** 2 + c ** 2:
    print ('TRIANGULO ACUTANGULO')


  if a == b == c:
    print ('TRIANGULO EQUILATERO')
  elif a == b or b == c or c == a:
    print ('TRIANGULO ISOSCELES')
