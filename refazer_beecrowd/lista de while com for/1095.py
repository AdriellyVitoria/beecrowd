def sequencia (): #funcao
  i = 1 #contador
  j = 60 #contador
  for c in range (j, -1, -5): #vai de j até 0, pulando em 5 
    print (f'I={i} J={c}') #saida
    i += 3 #aumentar o contador


sequencia () #chamar a função