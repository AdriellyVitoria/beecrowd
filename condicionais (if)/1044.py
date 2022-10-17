#ler dois valores inteiros:
a, b = str (input ()).split()

#classificando variaveis:
a = int (a)
b = int (b)

#verificar se os valores são multiplos:
if a % b == 0 or b % a == 0:
  print ('Sao Multiplos')
else:
  print ('Nao sao Multiplos')
