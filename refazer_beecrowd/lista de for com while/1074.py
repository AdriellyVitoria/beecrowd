valor = int (input ()) #entrada
contador = 1 #contador
while contador <= valor: #vai de 1 até valor
  contador += 1 #aumento do contador
  numero = int (input ()) #entrada
  if numero == 0: #se o numero for 0
    print ('NULL') #saida
  elif numero % 2 == 0: #se for par
    print ('EVEN',end=' ') #saida
  elif numero % 2 == 1: #se for impar
    print ('ODD',end=' ') #saida
  if numero > 0: #se for positivo
    print ('POSITIVE') #saida
  elif numero < 0: #se for negattivo
    print ('NEGATIVE') #saida
  