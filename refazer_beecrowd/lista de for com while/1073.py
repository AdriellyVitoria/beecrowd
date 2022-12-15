valor = int (input ()) #entrada
contador = 0 #contador
while contador <= valor: #só vai parar quando chegar no numero
  contador += 2 #aumento no contador
  
  if contador % 2 == 0 and contador <= valor: #verificar se é par e se é menor q o valor
    print (f'{contador}^2 = {contador ** 2}') #saida
    