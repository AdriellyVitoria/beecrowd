total = coelhos = ratos = sapos = 0 #contador
repeticao = int (input ()) #entrada
for c in range (0, repeticao): #de 0 até o numero recebindo
  quantidade, tipo = input ().split () #entrada
  quantidade = int (quantidade) #transformaçao para inteiro
  tipo = str (tipo).upper ()#transformaçao para letras maiuculas
  total += quantidade #somatorio
  if tipo == 'C': #verificando se o tipo é coelhos
    coelhos += quantidade #somatorio
  elif tipo == 'R': #verificar se o tipo é rato
    ratos += quantidade  #somatorio
  elif tipo == 'S': #verificar se o tipo é sapo
    sapos += quantidade #somatorio
 #saida   
print (f'''Total: {total} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {100 / total * coelhos:.2f} %
Percentual de ratos: {100 / total * ratos:.2f} %
Percentual de sapos: {100 / total * sapos:.2f} %''')

