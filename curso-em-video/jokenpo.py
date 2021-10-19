from random import randint 
opcoes = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0,2)

print('''
0 - Pedra
1 - Papel
2- Tesoura
''')
escolha = int(input('Qual a sua opção??\n'))
print(f'O jogador escolheu {opcoes[escolha]}')

if pc == 0: #Pc jogou PEDRA
    if escolha == 0: 
        print('EMPATE')
    elif escolha == 1: 
        print('JOGADOR GANHOU')
    elif escolha == 2: 
        print('JOGADOR PERDEU')
    else:
        print('JOGADA INVALIDA')
    
elif pc == 1: #Pc jogou PAPEL
    if escolha == 0:
        print('JOGADOR PERDEU')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('JOGADOR GANHOU')
    else:
        print('JOGADA INVALIDA')

elif pc == 2: #Pc jogou TESOURA
    if escolha == 0:
        print('JOGADOR GANHOU')
    elif escolha == 1:
        print('JOGADOR PERDEU')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')