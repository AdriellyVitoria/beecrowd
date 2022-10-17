#ler o tempo e a velocidade
tempo = int (input ())
velocidade = int (input ())

#distancia 
distancia = velocidade * tempo

#combutivel gasto 
gasto = distancia / 12

#saida do resultando 
print (f'{gasto:.3f}')
