def contagem (numero):
  for i in range (1, numero + 1):
    x(i)


def x (linha):
  giros = 1
  while giros <= linha:
    if giros < linha:
      print (giros, end= ' ')
    else:
      print (giros)
    giros += 1


valor = int (input ())
contagem (valor)