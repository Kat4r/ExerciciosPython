from random import *
alunos = []
for i in range(4):
     alunos.append(str(input(f'Digite o nome do {i+1}º aluno: ')))
shuffle(alunos)
print(f'O aluno escolhido será: {", ".join(map(str, alunos))}')
