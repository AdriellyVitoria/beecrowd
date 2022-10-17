#ler o valor em float
salario = float (input ())

#reajuste de 15%:
if salario <= 400:
  reajuste = salario / 100 * 15 
  soma = salario + reajuste
  print (f'''Novo salario: {soma:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: 15 %''')

#reajuste com 12%:
elif salario <= 800:
  reajuste = salario / 100 * 12
  soma = reajuste + salario
  print (f'''Novo salario: {soma:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: 12 %''')

#reajuste com 10%
elif salario <= 1200:
  reajuste = salario / 100 * 10
  soma = salario + reajuste
  print (f'''Novo salario: {soma:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: 10 %''')

#reajuste com 7%:
elif salario <= 2000:
  reajuste = salario / 100 * 7
  soma = salario + reajuste
  print (f'''Novo salario: {soma:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: 7 %''')

#reajuste com 4%:
elif salario >= 2000:
  reajuste = salario / 100 * 4
  soma = salario + reajuste
  print (f'''Novo salario: {soma:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: 4 %''')
