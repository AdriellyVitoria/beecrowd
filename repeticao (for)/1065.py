pares = 0 #contador
for c in range (1, 6): #vai de 1 até 5
  numero = int (input ()) #entrada
  if numero % 2 == 0: #verificar se é positivo
    pares += 1 #aumentar no contador
print (f'{pares} valores pares') #saida