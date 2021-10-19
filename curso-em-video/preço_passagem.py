distancia = int(input('Qual a distância da viagem?\n'))

if distancia < 200 or distancia == 200 :
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'O preço da sua viagem será de {preco}')