#valor, prestacao, dias_atraso
def calcular (x, y, z):
  dinheiro = total_prestacao = 0
  # Para pagamentos sem atraso, cobrar o valor da prestação. 
  if z == 0:
    print (f'valor a pagar {x}')
    dinheiro += x
    total_prestacao += y
    #Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
  if z > 0:
    multa = x + (100 // 3) #multa
    juros =  z * 1
    total = multa + juros
    print (f'vai tem uma multa de {100//3:.1f} que vai ficar de {multa}, por causa dos {z} dias em atraso terá juros de {juros} e o total a pagar é de {total}')
    dinheiro += x #acumuladores
    total_prestacao += y #acumuladores

  if x == 0:
    print (f'{dinheiro} e {total_prestacao}')

   
      
def rodar ():
  valor = 0
  while valor > 0:
    #pegar o valor q irá ser pago
    valor = int (input ())
    #o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
    #pegar a prestação e o numero de dias q está em atraso
    prestacao, dias_atraso = map (int, input ().split ())

    calcular (valor, prestacao, dias_atraso)


rodar ()
#passar para a fuçao de valor a pagar e devolver ao programar que ele foi chamando 
#dever pegar outro valor e as prestação até q seja imformando um valo igual a 0 para a prestação para encerra o programa