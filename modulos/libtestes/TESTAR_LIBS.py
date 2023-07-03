import testespy

item = testespy.itensRand()
print(item)

nomeJogador = testespy.nomesJogadoresRand()
print(nomeJogador)

amiga = testespy.nomesRand(sexo="f")
print(amiga)

amigo = testespy.nomesRand(sexo="m")
print(amigo)

idade = testespy.idadeRand()
print(idade)

time = testespy.timesRand()
print(time)

testespy.geradorMegasena(1)

carro = testespy.carrosRand()
print(carro)