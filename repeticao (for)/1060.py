positivo = 0 #contador
for c in range (1, 7): #girar 6 vezes
  numero = float (input ()) #entrada 
  if numero > 0: #se o valor for positivo
    positivo += 1 #contador
print (f'{positivo} valores positivos') #saida
