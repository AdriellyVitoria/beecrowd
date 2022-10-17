valor = int (input ()) #receber um valor
numero = 0 #contador
while numero < 6:
  if valor % 2 == 1: #verificar se é impar
      print (f'{valor}') #imprimir saida
      numero += 1 #soma parar para while
  valor += 1 #soma para pegar o proximo valor
  