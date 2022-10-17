repeticao = int (input ()) #entrada
for c in range (0, repeticao): #1 até repeticao
  valor = int (input ()) #entrada
  if valor == 0: #se o valor for 0
    print ('NULL') #saida em ingles 
  elif valor % 2 == 0: #verificar se é par e diferente de 0
    print ('EVEN',end=" ") #saida em ingles
  elif valor % 2 == 1: #verificar se é impar
    print ('ODD',end=" ") #saida em ingles
  if valor > 0: #verificar se é positivo
    print ('POSITIVE')#saida em ingles
  elif valor < 0:  #verificar se é negativo
    print ('NEGATIVE')#saida em ingles
