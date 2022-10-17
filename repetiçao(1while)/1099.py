teste = int (input ()) #recebr quatidade de teste
giros = impar = 0 #contadores
while giros != teste:
  x, y = map (int, input ().split()) #receber os numeros int
  giros += 1 #parar o while
  while x >= y: #verificar se x é maior
    y += 1 #pegar o sucessor Y
    if y % 2 == 1 and y < x: #verificar se é impar e menor q x
      impar += y #aquivar o numero
  while x <= y: #verificar se x é menor
    x += 1 #pegar o sucessor de x
    if x % 2 == 1 and x < y:#verificar se é impar e menor y
      impar += x #aquivar o numero
  print (impar) #saida
  impar = 0 #zera, para não somar todos os numeros impar
     