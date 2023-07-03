from modulos.libtestes import testespy as tpy


nomes = [tpy.nomesRand('f') for i in range(10)]

nomesupper = lambda lista: [nome.upper() for nome in lista]


print(nomesupper(nomes))