while True:
  ponto_1, ponto_2 = map (int, input (). split()) #receber os valores
  if ponto_1 == 0 or ponto_2 == 0: #condicao para parar
    break
  #verificar os quadrantes
  elif ponto_1 > 0 and ponto_2 > 0:
    print ('primeiro')
  elif ponto_1 < 0 and ponto_2 > 0:
    print ('segundo')
  elif ponto_1 < 0 and ponto_2 < 0:
    print ('terceiro')
  elif ponto_1 > 0 and ponto_2 < 0:
    print ('quarto')