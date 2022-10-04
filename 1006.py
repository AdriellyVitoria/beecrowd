#ler três valores (A,B e C)São três notas de um aluno 
A = float (input ())
B = float (input ())
C = float (input ())

#peso das notas, A = 2. B = 3. C = 5
peso_A = A * 2
peso_B = B * 3
peso_C = C * 5

#calcular a media do aluno 
media = (peso_A + peso_B + peso_C) / 10

#saida do resultado:
print (f'MEDIA = {media:.1f}')
