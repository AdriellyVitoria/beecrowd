repeticao = int (input ()) #entrada
for c in range (1, repeticao + 1):#de 1 até repeticao + 1
  numero_1, numero_2 = map (int, input ().split ()) # entrada de valores
  if numero_2 == 0: #se divisor for 0
   print ('divisao impossivel') #saida
  elif numero_1 / numero_2 or (numero_1 / numero_2) == 0:# se dividir e se o resultando for 0
    print (f'{numero_1 / numero_2:.1f}') #saida
 