#ler o codigo da peça1, o número, o valor. E o da peça2
peca1, numero1, valor1 = str (input ()).split()
peca2, numero2, valor2 = str (input ()).split()

#valores amazenados 
peca1 = int (peca1)
numero1 = int (numero1)
valor1 = round (float (valor1), 2)

peca2 = int (peca2)
numero2 = int (numero2)
valor2 = round (float (valor2), 2)

#somar das peças
somar_peca1 = numero1 * valor1
soma_peca2 = numero2 * valor2

#total das duas peças
total = somar_peca1 + soma_peca2

#saida do resultado
print (f'VALOR A PAGAR: R$ {total:.2f}')
