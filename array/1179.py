par = [] #criar listas
impar = [] #criar listas


#entrada de 15 numeros 
for i in range (15):
    numero = int (input ()) #entrada
     
#verificar se ele é par ou impar
    if numero % 2 == 0: 
        par.append(numero) #add numeros
    else:
        impar.append(numero) #add numeros

    if len(impar) >= 5 or i == 14: #imprimir os numeros impar
        for k, l in enumerate(impar): #pegar ´posição e o numero
            print (f'impar[{k}] = {l}') #saida
        impar = [] #zera listas

    if len(par) >= 5 or i == 14: #imprimir os numeros
        for c, j in enumerate(par): #pegar ´posição e o numero
            print (f'par[{c}] = {j}') #saida
        par = [] #zera listas