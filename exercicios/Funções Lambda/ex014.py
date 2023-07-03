from modulos.libtestes import testespy as tpy

itens = [tpy.itensRand() for i in range(50)]

tamanhofrase = lambda lista: [item for item in lista if len(item) >= 10]

print(len(tamanhofrase(itens)))