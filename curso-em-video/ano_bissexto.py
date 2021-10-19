ano = int(input('Digite qual ano voce deseja saber'))

if ano % 4 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')