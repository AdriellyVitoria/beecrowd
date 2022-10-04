#ler o valor inteiro do dinheiro
valor = int (input())

#separar a nota por de 100 a 1 real
#começar separando as notas de 100:
cem = int (valor / 100)

#para prosseguir vc pegar o valor completo, e diminuir pela as notas de 100 separanda. assim:
sobrou = valor - (cem * 100) 

#separa as notas de 50:
cinquenta = int (sobrou / 50) 

#pegar o valor q sobrou e diminuir pela a nota q saiu
sobrou1 = sobrou - (cinquenta * 50)

#separa as de 20:
vinte = int (sobrou1 / 20)

#diminuir os vinte q saiu
sobrou2 = sobrou1 - (vinte * 20)

#separa as notas de 10:
dez = int (sobrou2 / 10)

#diminiur as notas que sairam
sobrou3 = sobrou2 - (dez * 10)

#separa as notas de 5:
cinco = int (sobrou3 / 5)

#diminuir as notas que sairam
sobrou4 = sobrou3 - (cinco * 5)

#separa as notas de 2:
dois = int (sobrou4 / 2)

#diminuir as notas que sairam
sobrou5 = sobrou4 - (dois * 2)

#separa as moedas de 1 real:
real = int (sobrou5 / 1)

#saida do resultando 
print (f'{valor}')
print (f'{cem} nota(s) de R$ 100,00')
print (f'{cinquenta} nota(s) de R$ 50,00')
print (f'{vinte} nota(s) de R$ 20,00')
print (f'{dez} nota(s) de R$ 10,00')
print (f'{cinco} nota(s) de R$ 5,00')
print (f'{dois} nota(s) de R$ 2,00')
print (f'{real} nota(s) de R$ 1,00')
