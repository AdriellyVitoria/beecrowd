matriz = []
soma = cont = 0

operação = input().upper()
for i in range (12):
    lista = []
    for j in range (12):
        numero = float (input())
        lista.append(numero)

    matriz.append(lista)

começo = 11 #para começar o j
for i in range(1, 12): #vai até 11 a linha
    for j in range(começo, 12): #difinir o começo e o limitir é 11
        soma += matriz[i][j] #soma com o elemento nesta posição
        cont += 1 #acumulador
    começo -= 1 #diminuir o começo do j 

if operação == 'S': #verificar se é para soma
    print(f'{soma:.1f}') #saida
elif operação == 'M': #verificar se é para pegar a media
    print (f'{soma/cont:.1f}') #saida
