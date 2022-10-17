numero = int (input ()) #entrada
for c in range (0, numero + 1): #conta de 1 até 3
  nota1, nota2, nota3 = map (float, input ().split ()) #recebe notas
  media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10 #media
  print (f'{media:.1f}') #calculos e saida