valorcasa = int(input('Digite o valor da casa '))
salario = int(input('Qual o seu salario '))
anos = int(input('Em quantos anos deseja pagar '))

parcela = anos * 12
valortotal = valorcasa/parcela
porcento = salario * 0.30

print(f'Voce deverá pagar {valortotal} reais todo mês')

if valortotal > porcento or valortotal == porcento:
    print('Você não pode comprar a casa, sinto muito')
else:
    print(f'Você pode comprar a casa, parabéns')
