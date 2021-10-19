frase = str(input('Digite seu nome\n')).strip()
nometodo = (len(frase) - frase.count(' '))
primnome = frase.find(' ')

print(f'Seu nome em maiúsculo é {frase.upper()}')
print(f'Seu nome em minúsculo é {frase.lower()}')
print(f'Seu nome ao todo tem {nometodo} letras')
print(f'Seu primeiro nome tem {primnome} letras')