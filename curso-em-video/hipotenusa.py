from math import hypot
co = int(input('Digite o numero do cateto oposto'))
ca = int(input('Digite o numero do cateto adjacente'))
hip = hypot(co,ca)
print(f'A hipotenusa do triangulo {co}/{ca} é {hip}')