numero = maior = 0 #contador
while numero < 100:
  valor = int (input ()) #recebe o valor
  numero += 1 #aumento para parar o while
  if valor > maior: #verificar qual o maior
    maior = valor
    posicao = numero
    
#imprimir saida 
print (f'''{maior} 
{posicao}''')
  