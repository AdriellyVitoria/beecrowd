#ler um numero q vai indicar a linha da matriz [0 a 11]
#qual operação dever ser realizanda Soma ou Media
#mostras o calculo da opçao escolhinda 

operação = input ().upper() #receber S ou M

soma = 0 #acumulador
matriz = [] #criar lista
for i in range (12): #pegar as linhas
    linha = [] #criar lista e zera lista

    for j in range (12): #pagar as colunas
        valor = float (input ()) #receber os valores
        linha.append(valor) #add os valores

    matriz.append(linha[:]) #copiar a linha

if operação == 'S': #verificar
    print (f'{soma:.1f}') #saida
elif operação == 'M': #verificar
    print(f'{soma/12:.1f}') #saida
