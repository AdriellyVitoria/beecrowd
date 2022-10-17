#ler 3 imformações de animal.... sua formação, a divisão e sua alimetação:
nome1 =  str (input ()).lower().strip()
nome2 =  str (input ()).lower().strip()
nome3 =  str (input ()).lower().strip()

#as conseguecias para vertebrado:
if nome1 == 'vertebrado': 
  if nome2 == 'ave':
    if nome3 == 'carnivoro':
      resposta = 'aguia'
    elif nome3 == 'onivoro':
      resposta = 'pomba'
  elif nome2 == 'mamifero':
    if nome3 == 'onivoro':
      resposta = 'homem'
    elif nome3 == 'herbivoro':
      resposta = 'vaca'

#as conseguecias para invertebrado:
if nome1 == 'invertebrado':
  if nome2 == 'inseto':
    if nome3 == 'hematofago':
      resposta = 'pulga'
    elif nome3 == 'herbivoro':
      resposta = 'lagarta'
  elif nome2 == 'anelideo':
    if nome3 == 'hematofago':
      resposta = 'sanguessuga'
    elif nome3 == 'onivoro':
      resposta = 'minhoca'

  #imprimir resultando:
print (resposta)

