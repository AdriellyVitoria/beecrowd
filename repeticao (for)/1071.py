soma = 0 #contador
#entradas
inicio = int (input ())
final = int (input ())
if inicio > final: #trocar para pegar o menor numero
  trocar = final
  final = inicio
  inicio = trocar
for c in range (inicio + 1, final): #pegando os numeros
  if c % 2 == 1:#verificando se é impar
    soma += c #somar os impar
print (f'{soma}') #saida
