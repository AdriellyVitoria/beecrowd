#ler dois valores com float (nota1 e nota2), que são duas notas de um aluno
A = round (float (input ()), 2)
B = round (float (input ()), 2)

#peso das notas, nota1 = 3.5 e a nota2 = 7.5
peso_A = A * 3.5
peso_B = B * 7.5

#calcular a media do aluno 
media = (peso_A + peso_B) / 11

#saida do resultado
print (f'MEDIA = {media:.5f}')
