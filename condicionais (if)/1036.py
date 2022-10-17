#recebe 3 valores float 
a, b, c = str (input ()).split()

#declara variaveis 
a = float (a)
b = float (b)
c = float (c)

#classificando os if:
if a != 0:
  delta = b ** 2 - 4 * a * c 
  if delta >= 0:
    r1 = (-b + delta ** 0.5) / (2 * a)
    r2 = (-b - delta ** 0.5) / (2 * a)
    if r1 == r2:
      print (f'R1 = {r1:.5f}')
    else:
      print (f'R1 = {r1:.5f}')
      print (f'R2 = {r2:.5f}')
  else:
    print('Impossivel calcular')
else:
  print('Impossivel calcular')

