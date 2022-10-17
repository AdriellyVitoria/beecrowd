#ler um ddd inteiro
ddd = int (input ())

#disse de onde o ddd é... usando os ses
if ddd == 61:
  local = 'Brasilia'
elif ddd == 71:
  local = 'Salvador'
elif ddd == 11:
  local = 'Sao Paulo'
elif ddd == 21:
  local = 'Rio de Janeiro'
elif ddd == 32:
  local = 'Juiz de Fora'
elif ddd == 19:
  local = 'Campinas'
elif ddd == 27:
  local = 'Vitoria'
elif ddd == 31:
  local = 'Belo Horizonte'
else:
  local = 'DDD nao cadastrado'  
print (f'{local}')