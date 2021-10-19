salario = int(input('Digite o valor do seu salario'))

if salario > 1200:
    novosalario = salario * 1.10
else:
    novosalario = salario * 1.15

print(f'Seu salario com ajuste é de {novosalario} reais')