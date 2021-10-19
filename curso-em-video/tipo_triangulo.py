import math

l1 = int(input('Digite o lado 1 '))
l2 = int(input('Digite o lado 2 '))
l3 = int(input('Digite o lado 3 '))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    if l1 == l2 == l3:
        print(f'O triangulo PODE ser formado e será equilatero')
    elif l1 != l2 != l3 != l1:
        print(f'O triangulo PODE ser formado e será escaleno')
    else:
        print(f'O triangulo PODE ser formado isoceles')
else:
    print(f'O triangulo NAO PODE ser formado')
