pares = impar = positivos = negativos = 0 #contador
for c in range (1, 6): #vai de 1 até 6
  numero = int (input ()) #saida
  if numero % 2 == 0: #verificar se é par
    pares += 1  #aumento no contador
  if numero % 2 == 1:#verificar se é impar
    impar += 1 #aumento no contador
  if numero > 0: #verificar se é positivo
      positivos += 1 #aumento no contador
  if numero < 0: #verificar se é negativo
      negativos += 1 #aumento no contador
#saida
print (f'''{pares} valor(es) par(es)
{impar} valor(es) impar(es)
{positivos} valor(es) positivo(s)
{negativos} valor(es) negativo(s)''')
