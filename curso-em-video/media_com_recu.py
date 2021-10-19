nota1 = int(input('Digite sua nota da A1 '))
nota2 = int(input('Digite sua nota da A2 '))

media = (nota1+nota2)/2

if media < 5:
    print(f'REPROVADO')
elif media == 5 or media < 7 :
    print(f'RECUPERAÇÃO')
elif media == 7 or media > 7:
     print(f'APROVADO')