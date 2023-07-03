import random

numeros = []
for i in range(1,11):
    numeros.append(random.randint(0,999))

print(f"O maior valor encontrado na lista foi: {max(numeros)}\n"
      f"E o menor valor encontrado foi: {min(numeros)}")
