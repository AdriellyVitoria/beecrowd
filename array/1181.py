entradas =  int (input ())

numeros = []
menor = 0
posição = 1

for i in range (entradas):
    valor = map (int, input ().split())
    numeros.append(valor)

    if i == 0:
        menor = valor

for j, n in enumerate (entradas):
    
    if menor > numeros(-1):
        menor = j
        posição = n
        numeros.pop(-1)
    else:
        numeros.pop(-1)
    
print (menor, posição)