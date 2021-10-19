from datetime import date
atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}')

if idade == 18:
    print('Se aliste imediatamente')
elif idade<18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento ')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade>18:
    saldo = idade -18
    print(f'Você deveria ter se alistado a {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
