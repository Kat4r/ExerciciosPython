from modulos.libtestes import testespy as tpy

nomes = []

for i in range(10):
    nomes.append(tpy.nomesRand('f'))

print(nomes)

ordenadoAlfa = lambda lista: sorted([nome for nome in lista])

print(ordenadoAlfa(nomes))