def contagem (n):
  for c in range (1, n + 1):
    giros = 1

    while giros <= c:

      if giros < c:
        print (c, end=' ')
      else:
        print (c)

      giros += 1


numero = int (input ())

contagem(numero)