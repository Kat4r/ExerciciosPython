"""Escreva um programa Python que crie dois arrays: um array com os números de
1 a 5 e outro array com os números de 6 a 10. Em seguida, o programa deve
mesclar os dois arrays em um único array e imprimir o resultado."""
#é criado uma lista contendo numeros de 1 a 5
lista1 = list(range(1,6))

#é criado uma lista contendo numeros de 6 a 10
lista2 = list(range(6,11))

#é feita a união de maneira simplificada das listas criadas usando +
listaFormada = lista1 + lista2

#mostra o resultado das listas unificadas
print(listaFormada)

