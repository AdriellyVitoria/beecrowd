# def imprimir_listas (lista):
#     for item in lista:
#         print(item)


# valores1 = [1, 2, 3, 4, 5, 6]
# valores2 = [1, 2, 7, 4, 5, 6]
# valores3 = [1, 2, 8, 4, 5, 6]
# valores4 = [1, 2, 9, 4, 5, 6]
# valores5 = [1, 2, 0, 4, 5, 6]
# valores6 = [1, 2, 1, 4, 5, 6]

# imprimir_listas(valores1)
# imprimir_listas(valores2)
# imprimir_listas(valores3)
# imprimir_listas(valores4)
# imprimir_listas(valores5)
# imprimir_listas(valores6)


#quando i tive um o j vai tá em 1... quando i tive 1 j via tá em 2.... quando   
matriz = [] #criar lista
soma = cont = 0 #acumuladores
operação = input().upper() #pegar operação [S/M]

for i in range (12): #pegar linha
    linha = [] #criar lista e zera ela 

    for j in range (12): #pegar coluna 
        numero = float (input ()) ##pegar os numeros
        linha.append(numero) #add a lista
        if j > i: #se j for menor q i
            soma += numero #acumular em soma
            cont += 1 #cont para dividir
    matriz.append(linha[:]) #pegar os elementos da lista

if operação == 'S': #verificar
    print (f'{soma:.1f}') #saida
elif operação == 'M': #verificar
    print(f'{soma/cont:.1f}') #saida