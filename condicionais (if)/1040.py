l #ler 4 variaveis:
nota1, nota2, nota3, nota4 = str (input ()).split()

#classificação das variaveis:
nota1 = float (nota1)
nota2 = float (nota2)
nota3 = float (nota3)
nota4 = float (nota4)

#calcular pesos das notas:
peso1 = nota1 * 2
peso2 = nota2 * 3
peso3 = nota3 * 4
peso4 = nota4 * 1

#calcular media:
media = (peso1 + peso2 + peso3 + peso4 ) / 10

#resltando dos if:
if media >= 7.0:
  print (f'Media: {media:.1f}')
  print ('Aluno aprovado.')
elif media < 5.0:
  print (f'Media: {media:.1f}')
  print ('Aluno reprovado.')

#se o aluno tira uma nota entre 5.0 e 6.9 vai para o exame:
elif media >= 5.0 and media <= 7.0:
 
#o programar vai pergunta a do nota do exame
    nota_exame = float (input ())
    recalcular = (media  + nota_exame ) / 2
    print (f'Media: {media:.1f}')
    print ('Aluno em exame.')
    print (f'Nota do exame: {nota_exame:.1f}')
    if recalcular >= 5.0:
      print ('Aluno aprovado.')
    elif recalcular < 5.0:
      print ('Aluno reprovado')
    print (f'Media final: {recalcular:.1f}')
