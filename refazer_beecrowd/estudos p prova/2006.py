cha1 = 0
cha = int (input ())
while cha > 4 or cha < 0:
  print ('ERRO TENTE NOVAMENTE')
  cha = int (input ())
  
a, b, c, d, e = map (int, input ().split())

if a == cha:
  cha1 += 1
if b == cha:
  cha1 += 1
if c == cha:
  cha1 += 1
if d == cha:
  cha1 += 1
if e == cha:
  cha1 += 1


print (cha1)





