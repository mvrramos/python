num = int(input('Digite um numero para ser convertido: '))

print('''Escolha a base de conversao:
1- Binario
2- Octal
3- Hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'A conversão de {num} será {bin(num)[2:]}')
elif opcao == 2:
    print(f'A conversão de {num} será {oct(num)[2:]}')
elif opcao == 3:
    print(f'A conversão de {num} será {hex(num)[2:]}')