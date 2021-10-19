frase = str(input('Digite seu nome:\n')).upper().strip()
contagem = frase.count('A')
inicio = frase.find('A')+1
fim = frase.rfind('A')+1

print(f'A letra A aparece {contagem} vezes')
print(f'A primeira letra apareceu na posição {inicio}')
print(f'A ultima letra aparece na posição {fim}')