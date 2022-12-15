matriz = [] #criar lista
soma = cont = 0 #acumulador 
operação = input ().upper() #pegar opção

for i in range (12): #pegar a linha
    lista = [] #criar lista e zera
    for j in range (12): #pegar colunas
        numero = float (input ()) #pegar os numero s
        lista.append(numero) #add numero na lista
    matriz.append(lista) #add losta na matriz

limite = 11 #para diminuir o j
for i in range(11): #vai até 10 a linha
    for j in range(limite): #vai de 11 
        soma += matriz[i][j] #soma com o elemento nesta posição
        cont += 1 #acumulador
    limite -= 1 #diminuir limitar para o j diminuir tbm 

if operação == 'S': #verificar se é soma 
    print (f'{soma:.1f}') #saida
elif operação == 'M': #verificar se é media
    print (f'{soma/cont:.1f}') #saida
