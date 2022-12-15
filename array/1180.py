#ler um valor n q será o tamanha do verto x 

n = int (input ()) #entrada de valor

lista = input().split() #add os numero na lista, com o tamanho de n

for i in range (len(lista)): #percorre a lista
    lista[i] = int (lista[i]) #transforma os valores da int
    if i == 0: #pegar o menor valor
        menor = lista[i] #colocar para pegar o menor valor
        posição = i #pegar a posição do valor

    elif lista[i] < menor: #verificar se o proximo numero é menor q menor
        menor = lista[i] #trocar o numero de menor
        posição = i #pegar a posiçao

print (f'Menor valor: {menor}\nPosicao: {posição}')#saida