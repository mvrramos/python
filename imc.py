peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura '))

imc = peso/(altura**2)

print(f'{imc:.1f}')
if imc<18.5:
    print(f'Abaixo do peso')
elif 18.5<=imc<25 :
    print(f'Peso ideal')
elif 25<=imc<30 :
    print(f'Sobrepeso')
elif 30<=imc<40:
    print(f'Obesidade')
else:
    print(f'Obesidade morbida')