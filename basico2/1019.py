#ler os segundos em inteiro 
segundos = int (input ())

#transformação de segundos para minutos:
minutos = segundos // 60
segundos -= minutos * 60

#transformação de minutos para horas:
horas = minutos // 60
minutos -= horas * 60

#saida do resultando: 
print (f'{horas:.0f}:{minutos:.0f}:{segundos:.0f}')
