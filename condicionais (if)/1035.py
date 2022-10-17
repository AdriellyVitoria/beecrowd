#ler variaveis A, B, C, D
a, b, c, d = str (input ()).split()

#declarar variaveis:
a = int (a)
b = int (b)
c = int (c)
d = int (d)

#declarar se b é maior q c:
maior_bc = b > c

#declarar se d > a
maior_da = d > a

#soma das variaveis 
soma_cd = c + d
soma_ab = a + b
soma_total = soma_cd > soma_ab
positivo_cd = c >= 0 and d >= 0
par_a = a % 2 == 0

#declaro if:
if maior_bc and maior_da and soma_total and positivo_cd and par_a:
  print ('Valores aceitos')
else:
  print ('Valores nao aceitos')



