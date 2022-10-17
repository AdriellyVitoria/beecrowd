numero = int (input ()) #entrada
for c in range (2, numero + 1): #vai de 2 até 6
  if c % 2 == 0 and c <= numero:#verificar se é par, vai parar quando igual ao numero
    print (f'{c}^2 = {c ** 2}')#saida
