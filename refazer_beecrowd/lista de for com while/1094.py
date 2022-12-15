teste = int (input ()) #entrada
contador = total = coelho = ratos = sapos =  0 #contadores
while contador <= teste - 1: ##só vai parar quando chegar no teste
  contador += 1 # aumento no contador
  quantidade, tipo = (input ()).split() #entrda
  quantidade = int (quantidade) #transformando
  tipo = str (tipo).upper() #transformando e colocando para maiuculas
  total += quantidade # aumento no contador
  if tipo == 'C': #verificar o tipo 
    coelho += quantidade # aumento no contador
  elif tipo == 'R': #verificar o tipo
    ratos += quantidade # aumento no contador
  elif tipo == 'S': #verificar o tipo
    sapos += quantidade # aumento no contador

#saida    
print (f'''Total: {total} cobaias
Total de coelhos: {coelho}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {100 / total * coelho:.2f} %
Percentual de ratos: {100 / total * ratos:.2f} %
Percentual de sapos: {100 / total * sapos:.2f} %''')
