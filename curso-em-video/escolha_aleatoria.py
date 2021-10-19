from random import choice 
a1 = str(input('Qual o nome do 1° aluno'))
a2 = str(input('Qual o nome do 2° aluno'))
a3 = str(input('Qual o nome do 3° aluno'))
a4 = str(input('Qual o nome do 4° aluno'))
aluno = choice([a1,a2,a3,a4])
print(f'Entre os alunos {a1}, {a2}, {a3}, {a4} o escolhido é o {aluno}')