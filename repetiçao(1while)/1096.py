impar = 1 #contador para impar
j = 7 #contador de J
while impar <= 9: #só vai gira 9 vezes
  while j >= 5: 
    print (f'I={impar} J={j}') #saida do resultando
    j -= 1 #diminuir o j para parar o while
  j = 7 #repetir novamente o 2 while
  impar += 2 #aumenta para parar o 1 while
  