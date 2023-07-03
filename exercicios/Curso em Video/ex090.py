alunos = {}
escola = []
for i in range(3):
    alunos['nome'] = str(input("Digite o seu nome: "))
    alunos['nota'] = int(input("Digite sua nota: "))
    if alunos['nota'] >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    alunos['Situação'] = situacao
    escola.append(alunos.copy())

for i in escola:
    for keys, valores in i.items():
        print(f"\033[34m{keys.title()}\033[m \033[32m{valores}\033[m")
    print()

