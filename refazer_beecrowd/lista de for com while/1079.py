giros = int (input ('')) #entrada
contador = 1 #contador
while contador <= giros: #vai de 1 até giros
  contador += 1 #aumento no contador
  nota_1, nota_2, nota_3 = map (float, input ().split()) #entrada das notas
  media = (nota_1 * 2 + nota_2 * 3 + nota_3 * 5) / 10 #calcular media
  
  print (f'{media:.1f}') #saida
