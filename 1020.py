#ler a ideda de uma pessoa
idade_dias = int (input())

#ler a idade em ano:
ano = int (idade_dias / 365)

# mes = fica com oq sobrou é diminuir a idade_dias e retirar dos anos:
mes = idade_dias - (ano * 365)
mes1 = int (mes / 30)

#ler dias é oq fica:
dias = int (idade_dias - (ano * 365) - (mes1 * 30))

#saida de resultandos:
print (f'{ano} ano (s)')
print (f'{mes1} mes (es)')
print (f'{dias} dia (s)')
