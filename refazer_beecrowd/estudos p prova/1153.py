def fatorial (valor):
  giros = 1
  fatorial = 0

  for i in range (1, valor + 1):
    fatorial1 = valor * (valor - giros)
    fatorial += fatorial1
    giros += 1
  print (fatorial)


numero = int (input ())
fatorial (numero)