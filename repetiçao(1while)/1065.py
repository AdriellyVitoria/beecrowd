valores = 1
pares = 0

while valores <= 5:
  valor = int ( input ())

  if valor % 2 == 0:
    pares += 1

  valores += 1

print (f'{pares} valores pares')
