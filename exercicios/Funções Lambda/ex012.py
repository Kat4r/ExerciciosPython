from modulos.libtestes import testespy as tpy

nomes = [tpy.nomesRand('f') for i in range(10)]

letrasA = lambda lista: [nome for nome in lista if 'a' in nome]

print(letrasA(nomes))