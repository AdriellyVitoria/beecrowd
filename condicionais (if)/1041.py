#ler dois valores, q vai representar as coodenadas de um ponto em um plano.
eixo_x, eixo_y = str (input()).split()

#classificar variaveis:
eixo_x = float (eixo_x)
eixo_y = float (eixo_y)

#se x e y forem positivos
q1 = eixo_x > 0 and eixo_y > 0

#se x é negativo e y positivo
q2 = eixo_x < 0 and eixo_y > 0

#se x e y forem negativos
q3 = eixo_x < 0 and eixo_y < 0

#se x positivo e y negativo
q4 = eixo_x  > 0 and eixo_y < 0

#e o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”
#classificação dos if:
if eixo_x == eixo_y == 0:
  print ('Origem')
elif eixo_y == 0:
  print ('Eixo X')
elif eixo_x == 0:
  print ('Eixo Y')
elif q1:
  print ('Q1')
elif q2:
  print ('Q2')
elif q3:
  print ('Q3')
elif q4:
  print ('Q4')
