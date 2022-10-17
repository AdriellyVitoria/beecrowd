
while True:
  m, n = map (int, input ().split ()) #entrada dos valores
  if m <= 0 or n <= 0: #opcão para parar
    break
#para inverte os valores
  if m > n:
    trocar = n
    n = m
    m = trocar
  
  soma = 0
  while m <= n: 
    print(m, end=' ') #imprinte em ordem
    soma += m #soma os valores
    m += 1
  
  print(f'Sum={soma}')#imprimir saida
