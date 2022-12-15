# 4 = 4 * 3 * 2 * 1 = 24
giros = 1
numero = int (input ())
while numero > 1:
    numero *= (numero - giros)
    print (numero)
    giros += 1


    
