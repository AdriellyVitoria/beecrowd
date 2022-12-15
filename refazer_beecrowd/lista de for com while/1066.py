contador = par = impar = positivos = negativos = 0 #contadores

while contador <= 4: #vai parar qunaod chegar no 5
  contador += 1 #aumento no contador
  numero = int (input ()) #entrada

  if numero % 2 == 0: #verificar se é  par
    par += 1 #aumento no contador

  if numero % 2 == 1: #verificar se é impar
    impar += 1 #aumento no contador

  if numero > 0: #verificar se é positivo
    positivos += 1 #aumento no contador

  if numero < 0: #verificar se é negativos
    negativos += 1 #aumento no contador

print (f'{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{positivos} valor(es) positivo(s)\n{negativos} valor(es) negativo(s)') #saida
