from Objetos.coisasAleatorias import *

motor = Motorizacao(800,4.5)

print(motor.ligar_motor())

print(motor.desligar_motor())

carro = Carro2(500,4.5)

print(carro.set_combustivel(15))
print(carro.set_combustivel(45))
print(carro.set_combustivel(-1))