informacoes = {}
pessoas = [[],[]]
molieres, maisMedia, listaNomes = [],[],[]

import random

with open("nomes.txt", "r") as nomes:
    listaNomes = [i.strip() for i in nomes.readlines()]
print(listaNomes)

continuar = None

while continuar != "n":

    try:

        nome = input("digite seu nome: ").strip().title()
        informacoes["Nome"] = pessoas[0].append(nome)

        sexo = input("digite seu sexo [M/F]: ").lower()[0]
        while sexo not in "fFmM":
            sexo = input("digite seu sexo [M/F]: ").lower()[0]

        if sexo == "f":
            molieres.append(nome)

        informacoes["idade"] = pessoas[1].append(int(input("digite sua idade: ")))

        continuar = input("Deseja continuar? [S/N]: ").lower()[0]

        informacoes.copy()

    except Exception as e:
        print(e)
        print("\033[31mTentativa de caractere alfabetico em zona numérica.\033[m")

media = sum(pessoas[1]) / len(pessoas[1])

for pos,i in enumerate(pessoas[1]):
    if i > media:
        maisMedia.append(pessoas[0][pos])
        maisMedia.append(pessoas[1][pos])

print("~~" *30)

print("Pessoas cadastradas: ")
for k,v in informacoes.items():
    print(f"{k} : {v}")


print(f"A) Ao todo há {len(pessoas[0])} pessoas cadastradas\n"
      f"B) A média de idades equivale a {media:.2f} anos\n"
      f"C) As mulheres cadastradas foram: \033[32m{', '.join(map(str, molieres))}\033[m.\n"
      f"D) Lista de pessoas acima da média de idade {maisMedia}")












