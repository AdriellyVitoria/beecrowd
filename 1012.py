#difinir a str que contém três valores
a, b, c = str (input ()).split()

#a, b, c com ponto float e de dupla precisão:
a = round (float (a), 2)
b = round (float (b), 2)
c = round (float (c), 2)

# area do triangulo retangula(formula: b*h/2, obs: 
#( b é a base, h é altura) A por base e C altura.
triangulo = a * c / 2

#area do circulo de raio é C (formula: pi * raio ** 2)
circulo = 3.14159 * c ** 2

#area do trapezio (formula: ((B + b)* h) / 2)
#A e B são as bases e C é h de altura.
trapezio = ((a + b) * c )/ 2

#area quadrado (formula: l ** 2)
#B é o lado.
quadrado = b ** 2

#area do retângulo (formula: b * h)
#A e B são os lados
retangulo = a * b

#resultando do TRIANGULO:
print (f'TRIANGULO: {triangulo:.3f}')

#resultando do CIRCULO:
print (f'CIRCULO: {circulo:.3f}')

#resultando do TRAPEZIO:
print (f'TRAPEZIO: {trapezio:.3f}')

#resultando do QUADRADO:
print (f'QUADRADO: {quadrado:.3f}')

#resultando do RETANGULO:
print (f'RETANGULO: {retangulo:.3f}')
