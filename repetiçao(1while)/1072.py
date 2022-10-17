inteiro = outro = giros = 0 #contadores
numero_teste = int (input ()) #entrada 
while giros < numero_teste: #quantas vezes o programar vai girar
    valor = int (input ()) #entrada dos valores
    giros += 1 #aumento dos giros
    if valor >= 10 and valor <= 20: #verificar se está no intervalo
      inteiro += 1 #aumetar os valores 
    else: #verificando se não está no intervalo
      outro += 1 #aumentar os valores
#saida 
print (f'''{inteiro} in
{outro} out''')
