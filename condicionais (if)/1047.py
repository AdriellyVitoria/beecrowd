#ler 4 valores para hora e minutos iniciais, hora e minutos finais
horas_inicial, minutos_inicial, horas_final, minutos_final = str (input()).split()

#classificação das horas:
horas_inicial = int (horas_inicial)
minutos_inicial = int (minutos_inicial)
horas_final = int (horas_final)
minutos_final = int (minutos_final)

#soma hora e minuto inicial e hora e minutos finais.
jogo_inicial = horas_inicial * 60 + minutos_inicial
jogo_final = horas_final * 60 + minutos_final

#se o jogo terminar no outro dia 
if jogo_final <= jogo_inicial:
  jogo_final += 24 * 60
final_minutos_jogo = jogo_final - jogo_inicial
  
final_horas_jogo = final_minutos_jogo // 60
final_minutos_jogo -= final_horas_jogo * 60

#imprimir resultando:
print (f'O JOGO DUROU {final_horas_jogo} HORA(S) E {final_minutos_jogo} MINUTO(S)')