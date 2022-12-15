def converter(x, y):
  if x > 12:
    x -= 12
    tempo = 'PM'
  else:
    tempo = 'AM'
  
  saida(x, y, tempo)


def saida (x, y, tempo):
  print (f'{x}:{y} {tempo}')


def entrada ():
  hora, minutos = map (int, input ().split (':'))
  converter (hora, minutos)


entrada ()