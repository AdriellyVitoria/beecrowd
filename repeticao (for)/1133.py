valor1 = int (input ()) #entrada 
valor2 = int (input ()) #entrada
if valor1 > valor2:
  trocar = valor1
  valor1 = valor2
  valor2 = trocar

for c in range (valor1 + 1, valor2): #entre os valores recebidos
  if c % 5 == 2 or c % 5 == 3: #se o resto da divisao de 5 for 2 ou 3
    print (c) #saida
  