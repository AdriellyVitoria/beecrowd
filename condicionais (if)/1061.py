#ler a data e a hora inicial q vai começa o evento
_, dia_inicio = str (input ('')).split()
horas_inicial, minutos_inicial, segundos_inicial = str (input ()).split (' : ')

#ler a data e hora do final do evento:
_, dia_final = str (input ('')).split()
horas_final, minutos_final, segundos_final = map(int, input ().split(' : '))


#classificar as variaveis do inici da festa, como inteiros:
dia_inicio = int (dia_inicio)
horas_inicial = int (horas_inicial)
minutos_inicial = int (minutos_inicial)
segundos_inicial = int (segundos_inicial)

#classificação as variaveis do final da festa, como inteiros:
dia_final = int (dia_final)
horas_final = int (horas_final)
minutos_final = int (minutos_final)
segundos_final = int (segundos_final)

#deve-se transformar os valores, para realizar a conta como na questão 1047*
#calcular o dia:
dia = dia_final - dia_inicio

#soma hora e minuto inicial e hora e minutos finais.
evento_inicial = horas_inicial * 60 + minutos_inicial
evento_final = horas_final * 60 + minutos_final

final_minutos_evento = evento_final - evento_inicial
print (f'{evento_final, evento_inicial, final_minutos_evento}')


final_horas_evento = final_minutos_evento // 60
final_minutos_evento -= final_horas_evento * 60


#verificar o horario em segundos, o inicial e dps o final:
segundo_i = evento_inicial * 60 - segundos_inicial
segundo_f = evento_final * 60 - segundos_final
print (f'{segundo_i, segundo_f}')
#o evento em segundo
if segundo_f < segundo_i :
  segundo_f += 24 * 60 * 60
  dia -= 1

# Calcular duracao em segundos
Segundos = segundo_f - segundo_i

#imprimir resultando:
print (f'''{dia} dia(s)
{final_horas_evento} hora(s)
{final_minutos_evento} minuto(s)
{Segundos} segundo(s)''')

