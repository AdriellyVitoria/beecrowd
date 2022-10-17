#ler um valor float, para ser o salario
salario =  float (input ())

#imposto de rendan de acordo com o salario ganho:
#se ganha de 0 a 2000 imposto é isento:
if salario <= 2000:
  print ('Isento')

#se ganhar 2001 a 3000, imposto de 8%, mas tem que retirar os 2000, pois em cima dos 2000 não tem imposto
elif salario <= 3000:
  salario -= 2000
  imposto = salario / 100 * 8
  #resultando do imposto de 8%:
  print (f'R$ {imposto:.2f}') 

#se ganhar 3001 a 4500 vai pagar 18% de imposto, mas tbm tem q retira a parte dos impostos passandos.
elif salario <= 4500:
  #retirando do imposto isento
  salario -= 2000
  #retirando do imposto de 2001 a 3000
  imposto = 1000 / 100 * 8
  salario -= 1000
  #resltando do imposto:
  imposto += salario / 100 * 18
  print (f'R$ {imposto:.2f}')

# imposto acima de 4500, retira o imposto isento, 3000 e 4500:
elif salario > 4500:
  #retirada do imposto isento
  salario -= 2000

 #retirada do imposto de 3000 e calcular oq ficou:
  imposto = 1000 / 100 * 8
  salario -= 1000

 #retiranda do imposto de 4500 e calcular oq ficou:
  imposto += 1500 / 100 * 18
  salario -= 1500

  #resultando do imposto final
  imposto += salario / 100 * 28
  print (f'R$ {imposto:.2f}')
