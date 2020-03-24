vel = int(input('Qual a velocidade do carro?\n'))

if vel > 80:
    multa = (vel-80) * 7
    print(f'Você irá pagar {multa} reais de multa')
else:
    print('Muito bom, dirija com cuidado!')