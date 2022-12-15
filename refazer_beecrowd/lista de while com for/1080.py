def maior (): #função
  maior = posicao = giros= 0 #contadores
  for c in range (0, 100): #vai de de 1 até 100
    numero = int (input ()) #entrada
    giros += 1 #auemnto no giro
    if numero > maior: #pegar o maior numero
      maior = numero #recebe o maior
      posicao = giros #pegar a posição
  print (f'{maior}\n{posicao}') #saida
    


maior () #chamar a função
