from classes import *
from random import randint

num = 5
num1 = 10
print(num1 + num)
print(num - num1)
print(num * num1)
print(num / num1)

nome = 'João'
sobrenome = 'Silva'
print(f"{nome} {sobrenome}")

estaChovendo = False
print("Está chovendo leve um guarda-chuva" if estaChovendo else "Dia limpo")

vinicius = Pessoa("Vinicius", 23)
vinicius.dados()

numeros = list(range(50))
numeros.append(5)
numeros.pop(15)
numeros.remove(10)
numeros.insert(26,'aiiiiii')
print(numeros)

js = "JavaScript"
print(f"{js.count('a')}")

print("É maior de idade" if 18 >= 18 else "É menor de idade")

print("Numeros iguais" if 10 == 10 else "Numeros distintos")


carro = Carro("Ford", "GT", 2005)

carro.cor = 'Vermelho com preto'
carro.mostrar_dados()

frutas = ['banana','limao','tomate','alfacel']


print("\nfrutas com For")
for fruta in frutas:
    print(fruta)

print("\nfrutas com While")
"""c = 0
while c <= len(frutas):
    print(frutas[c])
    c+=1"""
print()

numeros = '1234'
numerosINT = int(numeros)

print(numeros + numeros)
print(numerosINT + numerosINT)

nome = "vinicius paulo de oliveira dos santos".title()
print(nome)

numerosrand = [randint(1,50) for i in range(25)]
print(max(numerosrand))
print(min(numerosrand))

numero = input("Digite numeros: ")
print(len(numero))



