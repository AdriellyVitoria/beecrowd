impar = giros = 1 #contador vai receber 1
somar = 0 #contador de soma vai receber 0
j = 7 #contador de j vai recebe 7
while impar <= 9: #só vai gira 9 vezes
  while giros <= 3:#só vai girar 3 vezes
    print (f'I={impar} J={j}') #imprimir saida
    j -= 1 #diminuir 1 no j
    giros += 1 #aumenta 1 no giro
  somar += 2 #aumenta 2 em soma
  j = 7 + somar #aumenta o j mais a soma
  impar += 2 #pegar os numeros impar
  giros = 1 #contar os giros

