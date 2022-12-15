def contador (): #função 
  fora = dentro = 0 #vai receber 0
  repetiçao = int (input ()) #entrada do numero de repeticao do programa
  for c in range (0, repetiçao): #vai de 1 até o numero de repeticao
    numero = int (input ()) #entrada dos outros numeros
    if numero >= 10 and numero <= 20: #verificar se está no intervalo
      dentro += 1 #aumento no contador 
    else: #se não
      fora += 1 #aumento no contador
  print (f'{dentro} in\n{fora} out') #saida
  
   
contador () #chamar a função
