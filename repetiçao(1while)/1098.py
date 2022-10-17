impar = giros = 0 #contador
j = 1 #j vai recebe 1
soma = 0.2 #soma vai recebe 0.2

while impar <= 2: #só vai parar qunado impar chegar a 2.0
  while giros < 3: #só vai girar 3 vezes

    if impar == 0 or impar == 2.0 or impar == 1.0: #verificar, para arrumar as casas decimal
      print (f'I={impar:.0f} J={j:.0f}') #imprimir saida com zero casa decimal

    elif impar != 0 or impar != 2.0 or impar != 1.0: #verificar, para arrumar as casas decimal
      print (f'I={impar:.1f} J={j:.1f}') #imprimir saida só com uma casa decimal

    j += 1 #aumenta 1 no j
    giros += 1 #contar os giros para encerrar o 2 while

  giros = 0 #zera para voltar ao 2 laço
  #round para limitar a casa decimal.
  j = round(1 + soma, 1) 
  soma = round(soma + 0.2, 1)
  impar = round (impar + 0.2, 1)