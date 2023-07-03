alunos = int(input("Digite a quantidade de alunos: "))+1

dados, dado = [],[]

for i in range(1,alunos):
    print(f"\nDados do {i}º  aluno:")
    dado.append(input("Nome do aluno: ").strip().title())
    dado.append(int(input("Nota na primeira matéria: ")))
    dado.append(int(input("Nota na segunda: ")))
    dados.append(dado[:])
    dado.clear()


print("-=" *10, "Escola Dolorosa aiuiaiui", "=-"*10,"\n")
for alunos in dados:
    print(f"\033[34mNome:\033[m {alunos[0]:15s} \033[34mMédia:\033[m {(alunos[1] + alunos[2]) / 2:5.2f}")
print("-="*32,end='-')

escolha = float("inf")
while escolha != 998:
        escolha = int(input("\nQuer mostrar a nota de qual aluno? \033[31m[ 999 ]\033[m para parar: ")) - 1
        print(f"\nAs notas de {dados[escolha][0]} foram \033[32m{dados[escolha][1]}\033[m e \033[32m{dados[escolha][2]}\033[m")

print("Planilha de alunos encerrada!")

