numero_inicial, numero_acao = map (int, input ().split ()) #entrada

abas = numero_inicial #acumulador
giros = 0  #contador

while giros < numero_acao: #vai até numero de acao
  giros += 1 #aumento no contador
  acao = input () #recebe acao

  if acao == 'fechou': #verificar altenativa
    abas -= 1 #diminuir no acumulador
    abas += 2 #aumenta no acumulaodor

  elif acao == 'clicou': #verificar altenativa
    abas -= 1 #diminuir no acumulador

print (f'{abas}') #saida de abas
