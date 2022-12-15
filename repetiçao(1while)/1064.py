valores = 1 #somar mais 1 a valores, para ele parar meu while
positivos =  total = 0 #a contagem de numeros positivos e soma todos os valores positivos
while valores <= 6: #vai rodar só até o 6
  valor = float (input ()) #recebe os numeros
  valores += 1 
  if valor > 0: #saber quais são os numeros positivos
    total += valor 
    positivos += 1
  
media = total / positivos  #calculto para media
print (f'''{positivos} valores positivos
{media:.1f}''') #imprimir resultando 