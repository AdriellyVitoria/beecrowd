matriz = [] #criar lista
soma = 0
numero = 12
operação = input().upper()
for i in range(12): #pegar as linhas
    linha = [] #criar lista e zera lista

    for j in range (12): #pagar as colunas
        valor = float (input ()) #receber os valores
        linha.append(valor) #add os valores
        # for a, b in enumerate (linha):
        #     if i == 1 or i >= 11:
        #         soma += b
        matriz.append(linha[:]) #copiar a linha
        parar = 1
for linha in matriz:
    for valor in range (numero, parar):
        soma += linha[valor]
        parar += 1


if operação == 'S': #verificar
    print (f'{soma:.1f}') #saida
elif operação == 'M': #verificar
    print(f'{soma/66:.1f}') #saida
     