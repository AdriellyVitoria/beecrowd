repeticao = int (input ()) #entrada
contador = 0 #contador
while contador <= repeticao: #vai até repeticao
  contador += 1 #aumento no contador
  numero_1, numero_2 = map (int, input ().split()) #entrada
  if numero_2 == 0: #verificar se o numero2 é 0
    print ('divisao impossivel') #saida
  elif numero_1 / numero_2 or (numero_1 / numero_2) == 0: #verificar se dividr
    print (f'{numero_1 / numero_2:.1f}') #saida
  
