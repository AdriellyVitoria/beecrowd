#ler duas horas
hora_inicia, hora_final = str (input ()).split()

#classificar as variaveis:
hora_inicia = int (hora_inicia)
hora_final = int (hora_final)

#ele pode termina no outro dia.
# se o final for <= que o inicio somar 24 ao final.
if hora_final <= hora_inicia:
  hora_final = hora_final + 24

final_jogo = hora_final - hora_inicia
print (f'O JOGO DUROU {final_jogo} HORA(S)')
