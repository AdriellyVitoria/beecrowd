n = int(input())
# giros = 1

# for j in range(n):
#     resu = 1
#     print (giros, end= ' ')
#     for i in range(3):      
#         if i == 0:            
#             resu = giros * giros
#             print (resu, end=' ')
#         elif i < 2:
#             resu *= giros
#             print (resu, end=' ')
#         if i == 2:
#             print ()
#             giros += 1
for i in range(1, n + 1):
    print(f'{i} {i ** 2} {i ** 3}')
