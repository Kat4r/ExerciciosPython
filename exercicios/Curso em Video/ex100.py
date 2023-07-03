import random
def sorteio():
    numeros = []
    for i in range(5):
        numeros.append(random.randint(0,100))
    return numeros

def numPar():
    parImpar = [[],[]]
    for num in sorteio():
        if num % 2 == 0:
            parImpar[0].append(num)
        else:
            parImpar[1].append(num)

    print(f"os numeros pares desse sorteio foram {', '.join(map(str, sorted(parImpar[0])))}\n"
          f"os numeros impares desse sorteio foram {', '.join(map(str, sorted(parImpar[1])))}\n"
          f"A soma de todos os pares é {sum(parImpar[0])} e de todos os impares é {sum(parImpar[1])}")
numPar()



