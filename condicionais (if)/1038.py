#ler duas variaveis codigo e quantidade:
codigo, quantidade = str (input ()).split()

#separando as variaveis:
codigo = int (codigo)
quantidade = int (quantidade)
#tenho q separa os preços e fazer multiplicação pelo os preços das coisas:
cachorro_quente = quantidade * 4.00
salada = quantidade * 4.50
bancon = quantidade * 5.00
torrada = quantidade * 2.00
refrigerante = quantidade * 1.50

#os if:
if codigo == 1:
  print (f'Total: R$ {cachorro_quente:.2f}')
elif codigo == 2:
  print (f'Total: R$ {salada:.2f}')
elif codigo == 3:
  print (f'Total: R$ {bancon:.2f}')
elif codigo == 4:
  print (f'Total: R$ {torrada:.2f}')
elif codigo == 5:
  print (f'Total: R$ {refrigerante:.2f}')
