giros = vitoria_inter = vitoria_gremio =  empates = 0    
novo = 1
while novo == 1:
    inter, gremio = map(int, input().split())
    if inter == gremio:
        empates += 1
    elif inter > gremio:
        vitoria_inter += 1
    else:
        vitoria_gremio += 1   
    novo = int(input())
    giros += 1
    if novo == 2:
        for i in range(giros):
            print('Novo grenal (1-sim 2-nao)')
        print(f'{giros} grenais\nInter:{vitoria_inter}\nGremio:{vitoria_gremio}\nEmpates:{empates}')       
        if vitoria_gremio > vitoria_inter:
            print ('Gremio venceu mais')
        elif vitoria_inter > vitoria_gremio:
            print('Inter venceu mais')
        else:
            print('Nao houve vencedor')