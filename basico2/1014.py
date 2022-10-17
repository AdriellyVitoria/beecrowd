#calcule o consumo médio de um automóvel 
#a distância (km) total será inteiro, representando pelo o x
x = int (input ())
#o combustível gasto (em real), representando pelo o y
y = float (input ()) 
#formula para calcular o consumo:
consumo = x / y
#saida do resultando:
print (f'{consumo:.3f} km/l')
