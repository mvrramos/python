n = str(input('Digite o nome completo:\n')).strip()
nome = n.split()

print(nome)
print(f'O primeiro nome é {nome[0]}')
print(f'O ultimo nome é {nome[len(nome)]-1}')
