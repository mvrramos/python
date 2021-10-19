from time import sleep

preco = int(input('Digite o preço do produto '))
print('Digite:')
print('1- Dinheiro/Cheque')
print('2- A vista ')
print('3- 2x no cartão')
print('4- 3x ou mais no cartão')

sleep (5)

pagamento = int(input('Qual das formas de pagamento acima???? '))

if pagamento == 1:
    preco = preco * 0.9
    print(f'Você tem 10% de desconto e irá pagar {preco} reais')
elif pagamento == 2:
    preco = preco *0.95
    print(f'Você tem 5% de desconto e irá pagar {preco} reais')
elif pagamento == 3:
    print(f'Você irá pagar o preço normal de {preco} reais')
elif pagamento == 4:
    preco = preco * 1.20
    print(f'Você terá juros de 20% e pagará {preco} reais')
