while True:
  #valida as notas separadamente
  nota1 = float (input ()) #entrada da primeira nota
  while nota1 > 10 or nota1 < 0: #verificar se é valida
    print ('nota invalida') 
    nota1 = float (input ('tente: ')) #perguntar até o usuario colocar uma nota valida

  nota2 = float (input ())#entrada da segunda nota
  while nota2 > 10 or nota2 < 0:
    print ('nota invalida')
    nota2 = float (input ())#perguntar até o usuario colocar uma nota valida
  
  media = (nota1 + nota2) / 2 #calcular a media
  print (f'media = {media:.2f}') #saida de resultando
  break #parar o programa
