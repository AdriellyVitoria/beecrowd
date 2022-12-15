giros = vitoria_inter = vitoria_gremio = empates = 0
def chamar(inter, gremio):
    global giros, vitoria_inter, vitoria_gremio, empates
    if inter == gremio:
        empates += 1

    if inter > gremio:
        vitoria_inter += 1

    if gremio > inter:
        vitoria_gremio += 1

    novo = int(input())
    giros += 1
     
    if novo == 1:      
        x, y = map(int, input().split())
        chamar(x, y)
    else:
        saida()

def saida():
    for i in range(giros):
        print('Novo grenal (1-sim 2-nao)')

    print(f'{giros} grenais\nInter:{vitoria_inter}\nGremio:{vitoria_gremio}\nEmpates:{empates}')

    if vitoria_gremio > vitoria_inter:
        print ('Gremio venceu mais')
    elif vitoria_inter > vitoria_gremio:
        print('Inter venceu mais')
    else:
        print('Nao houve vencedor')


x, y = map(int, input().split())
chamar(x, y)