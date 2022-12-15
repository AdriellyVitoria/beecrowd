linha = int(input())
lista = []
saida =[]
#A i-ésima linha seguinte contém 0 se não existe mina na i-ésima célula do tabuleiro e 1 se existe uma mina na i-ésima célula do tabuleiro.


for i in range (linha):
    numeros = int(input())
    lista.append(numeros)

print()


   
# for i, j in enumerate (lista):
#     while len(lista) > i:
#         if  j == 0 or (lista[i + 1]) == 1:
#             lista[i] = 1
#         elif j == 1 or (lista[i + 1]) == 1:
#             lista[i] = 2

#         break
