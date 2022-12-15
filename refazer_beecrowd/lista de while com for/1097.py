def sequencia ():
  i = 1 #contador 
  j = 7 #contador
  for c in range (i, 10, 2): #vai de 1 até 9, pulndo em 2
    giros = 1 # contador
    while giros <= 3: #vai de 1 até 3
      giros += 1 #aumento no contador
      print (f'I={c} J={j}') #saida
      j -= 1 #diminuir no contador
    j += 5 # aumento no contador
 


sequencia () #chamar função