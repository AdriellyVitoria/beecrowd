def soma (): #funçao
  repeticao = int (input ()) #receber o numero de repetição
  for c in range (0, repeticao): # vai de 1 até o numero de entrada
    acum = 0 #acumulador
    numero1, numero2 = map (int, input ().split()) #entrada
    if numero1 > numero2: #fazer a troca
      trocar = numero2
      numero2 = numero1
      numero1 = trocar
    while numero1 <= numero2: #
      numero1 += 1 #pegar os numeros do meio
      if numero1 % 2 == 1 and numero1 < numero2: #verificar se é impar e menor q o numero2
        acum += numero1 #acumular
    print (acum) #saida
    


soma () #chamar a função