contador = positivos = 0 #condadores
while contador <= 5: #até chegar em 6
  contador += 1 #aumentono contador 
  numero = float (input ()) #entrada
  if numero > 0: #verificar se é possitivo
    positivos += 1 #aumentono contador
print (f'{positivos} valores positivos') #saida
