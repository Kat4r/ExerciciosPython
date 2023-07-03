def gerarCPF():
    from random import randint
    cpf = [randint(0, 9) for i in range(9)]
    cpfcalculo1 = []
    c = 10
    buscador = 0
    while c <= 10 and c >= 2 :
        cpfcalculo1.append(cpf[buscador] * c)
        buscador+=1
        c-=1
    somacpf = sum(cpfcalculo1)

    restocpf = somacpf % 11
    if restocpf < 2:
        cpf.append(0)
    else:
        digito1 = 11 - restocpf
        cpf.append(digito1)

    cpfcalculo = []
    c = 11
    buscador = 0
    while c <= 11 and c >= 2 :
        cpfcalculo.append(cpf[buscador] * c)
        buscador+=1
        c-=1
    somacpf = sum(cpfcalculo)

    restocpf = somacpf % 11
    if restocpf < 2:
        cpf.append(0)
    else:
        digito1 = 11 - restocpf
        cpf.append(digito1)
    return cpf

cpf = gerarCPF()

print(''.join(map(str , cpf)))
