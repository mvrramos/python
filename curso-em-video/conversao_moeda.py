# Conversor de moedas
reais = float(input('Digite quantos reais você tem na carteira R$\n'))
dolar = float(input('Digite quanto está o dólar\n'))
conv = reais/dolar
print(f'Você pode comprar R${conv: .2f} dólar(es) com R${reais: .2f} reais')