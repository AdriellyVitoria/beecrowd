#para tem 99 posições, mostrando do numero até 0:
lista = [] #criar lista
valor_x = float (input ()) #entrada


for i in range (100): #vai de o até 99
    lista.append(valor_x) #add o valor
    valor_x /= 2 #pegar metade do valor


for i, j in enumerate(lista): #posiao e o valor
    print (f'N[{i}] = {j:.4f}') #saida
