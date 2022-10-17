#ler o numero de um funcionario, o numero de horas trabalhada, valor que recebe por hora 
numero_funcionario = int (input ())
horas_trabalhadas = int (input ())
valor_recebe_hora = float (input ())

#calcular as horas de trabalho para ver quanto ele ganhar
soma = horas_trabalhadas * valor_recebe_hora

#saida do resultando 
print (f'NUMBER = {numero_funcionario}')
print (f'SALARY = U$ {soma:.2f}')
