#ler o  nome do vendedor, o salario fixo, e o total de vendas do mês (em dinheiro)
nome = str (input())
salario = round (float (input ()), 2)
vendas = round (float (input ()), 2)

#o vendedor ganhar 15% de comissão em suas vendas
comissão = vendas / 100 * 15

#total para receber
total = salario + comissão

#saida do resultando 
print (f'TOTAL = R$ {total:.2f}')
