matriz = [] #criar lista

operação = input ().upper() #pegar a operação
soma = cont = 0 #acumulador
for i in range (12): #pegar a linha
    lista = [] #criar lista e zera
    for j in range (12): #pegar a coluna
        numero = float (input ()) #pegar o numero
        lista.append(numero) #add o numero
        if j < i: #verificar se i é maior q j
            soma += numero #acumular numero
            cont += 1 #acumulador no cont

    matriz.append(lista) #add a lista

if operação == 'S': #verificar se é soma 
    print (f'{soma:.1f}') #saida
elif operação == 'M': #verificar se é media
    print (f'{soma/cont:.1f}') #saida
