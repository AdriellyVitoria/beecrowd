valor1, valor2, valor3 = str (input ()).split()

#classificar variaveis 
valor1 = int (valor1)
valor2 = int (valor2)
valor3 = int (valor3)

#verificando se valor1 é o maior. usando if:
if valor1 >= valor2 and valor1 >= valor3:
  maior = valor1

#verificando quem é o do meio, logo oq ficar será o menor.
  if valor2 >= valor3:
   meio = valor2
   menor = valor3
  else:
    meio = valor3
    menor = valor2
#caso, o numero maior vou o valor2. seguir os if:
elif valor2 >= valor1 and valor2 >= valor3:
  maior = valor2

#verificando quem é o do meio e o menor:
  if valor1 >= valor3:
    meio = valor1
    menor = valor3
  else:
    meio = valor3
    menor = valor1
    
#verificando se o maior e o ultimo valor:
elif valor3 >= valor1 and valor3 >= valor2:
  maior = valor3

#verificando quem é o do meio e o menor:
  if valor1 >= valor2:
    meio = valor1
    menor = valor2
  else:
    meio = valor2
    menor = valor1

#os valores do menor para o maior:
print (f'''{menor}
{meio}
{maior}''')
print ()
#os valores na sequência como foram lidos.
print (f'''{valor1}
{valor2}
{valor3}''')