idade = int(input('Digite sua idade '))

if idade < 9 or idade == 9:
    print(f'MIRIM')
elif idade < 14 or idade == 14 :
    print(f'INFANTIL')
elif idade < 19 or idade == 19:
    print(f'JUNIOR')
elif idade < 20 or idade == 20:
    print(f'SÊNIOR')
elif idade > 20:
    print(f'MASTER')