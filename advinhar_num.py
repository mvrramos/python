from random import randint

pc = randint(0,5)
num = int(input('Qual numero o pc está pensando?\n'))

if num == pc:
    print(f'Você acertou, pensei no {pc} e você colocou {num}')
else:
    print(f'Você errou, pensei no {pc}')
