acumulador = 0
numero_1 =  int (input ())
numero_2 = int (input ())

if numero_1 > numero_2:
  trocar = numero_2
  numero_2 = numero_1
  numero_1 = trocar


while numero_1 < numero_2:
  if numero_1 < 0:
    numero_1 -= 1
  elif numero_1 % 2 == 1:
    acumulador += numero_1
    
  numero_1 += 1
print (acumulador)