positivos = acumulador = 0 #contador e acumulador
for c in range (0, 6): #vai até 6
  numero = float (input ()) #entrada
  if numero > 0: #verificar se é positivo
    positivos += 1 #contador
    acumulador += numero #acumulador
    media = acumulador / positivos #calcular media
print (f'{positivos} valores positivos\n{media:.1f}') #saida
