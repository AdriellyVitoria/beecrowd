contador = pares = 0  #contadores
while contador <= 4: #vai sí até 5
  contador += 1 #aumento no contador
  valor = int (input ()) #entrda
  if valor % 2 == 0: #verificar se é par
    pares += 1 #aumento no contador
print (f'{pares} valores pares') #saida
