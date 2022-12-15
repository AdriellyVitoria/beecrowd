
lista = [] #criar lista

valor_t = int (input ()) #entrada de valor
n = 0 #contador
for i in range (1000): #vai de 0 até 999
    lista.append(n) #add n na lista
    n += 1 #aumento no contador
    if n > (valor_t - 1): #verificar
        n = 0 #zera

for i, j in enumerate(lista): #imprimir a posição e os numero (0 até valor_t - 1)
    print (f'N[{i}] = {j}') #saida
