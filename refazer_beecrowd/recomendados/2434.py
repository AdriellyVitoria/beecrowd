#Saldo do vovô

dias, saldo_inicial = map (int, input ().split ()) #entrada 

giros = menor = 0 #contador
saldo = saldo_inicial #acumulador

while giros < dias: #parada
  giros += 1 #aumento no contador

  saldo_ = int (input ()) #entrada

  if menor == 0:   #menor saldo da conta
    menor = saldo 
   
  if saldo < menor: #salvar o menor saldo
    menor = saldo
  
  if saldo_ >= 0: #positivo, deposito
    saldo += saldo_

  if saldo_ <= 0: #negativo, retiranda
    saldo += saldo_

print (menor) #saida
  