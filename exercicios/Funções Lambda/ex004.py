from modulos.libtestes import  testespy as tpy

nomes = []
for i in range(5):
    nomes.append(tpy.nomesRand('f'))

tamanhopalavra = lambda lista: [len(nome) for nome in lista]

print(nomes)
print(f"{', '.join(map(str, tamanhopalavra(nomes)))}")