#ler a data e a hora inicial q vai começa o evento
_, dia_inicio = str (input ('')).split()
horas_inicial, minutos_inicial, segundos_inicial = map(int, input ().split(' : '))


#ler a data e hora do final que vai terminar o evento:
_, dia_final = str (input ('')).split()
horas_final, minutos_final, segundos_final = map(int, input ().split(' : '))

dia_inicio = int (dia_inicio)
dia_final = int (dia_final)

#deve-se transformar os valores, para realizar a conta como na questão 1047*

#trans horas para minutos:
minutos_inicial += horas_inicial * 60
minutos_final += horas_final * 60

#trans minuto para segundo:
segundos_inicial += minutos_inicial * 60
segundos_final += minutos_final * 60

#calcular o dia:
dia = dia_final - dia_inicio

if segundos_final < segundos_inicial :
  segundos_final += 24 * 60 * 60
  dia -= 1

# Calcular duracao em segundos
segundos = segundos_final - segundos_inicial

#destrans os segundos 
duracao_minutos = segundos // 60
segundos -= duracao_minutos * 60

duracao_hora = duracao_minutos // 60
duracao_minutos -= duracao_hora * 60

#imprimir resultando:
print (f'''{dia} dia(s)
{duracao_hora} hora(s)
{duracao_minutos} minuto(s)
{segundos} segundo(s)''')
