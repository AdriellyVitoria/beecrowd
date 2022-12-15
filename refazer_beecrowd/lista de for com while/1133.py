numero_1 = int (input ()) #entrada
numero_2 = int (input ()) #entrada

if numero_1 > numero_2: #trocar os valores
  trocar = numero_1
  numero_1 = numero_2
  numero_2 = trocar

while numero_1 < numero_2: #sói vai parar quando numero1 for maio q numero2
  
  if numero_1 % 5 == 2 or numero_1 % 5 == 3: #verifcar 
    print (numero_1) #saida
  
  numero_1 += 1 #aumento para pegar os numero do meio
