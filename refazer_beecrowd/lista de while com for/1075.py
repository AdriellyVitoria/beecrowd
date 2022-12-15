def resto (): #funçao
  numero = int (input ()) #entrada
  for c in range (1, 10000): #pegar de até 10000
    if c % numero == 2: #verificar se o resto dividido pela q entrada da 2
      print (c) #saida
  

resto ()#chamar a função