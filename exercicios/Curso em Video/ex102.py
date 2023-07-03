def fatorial(num, show=False):
    """
    Calculadora de fatoriais

    :param num: Recebe um numero que é feita a conta fatorial
    :param show: variavel booleana de True ou False, serve somente para ignorar ou não a conta feita
    """

    num_lista = []
    soma = 1
    for i in range(num, 1, -1):
        num_lista.append(i)

    if show:
        for numeros in num_lista:
            print(f"x {numeros}", end=" ")
            soma = soma * numeros
        return f"= {soma}"

    else:
        for numeros in num_lista:
            soma = soma * numeros
        return soma


fatorial(int(input('Digite um numero: ')), show=True) #show=False