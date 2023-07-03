def fibonacci(n_termos):
    """
    Na matemática, a sucessão de Fibonacci (ou sequência de Fibonacci), é uma sequência de números inteiros,
    começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores.

    :param n_termos: termos a serem mostrados em uma sequencia de fibonacci
    :return:
    """
    antes = ultimo = 1
    soma = []
    c = 0

    if n_termos == 1:
        print('\033[31m', '1')
    elif n_termos == 0:
        print('Esse numero não possui sequencia de fibonacci')
    else:
        print('\033[31m', '1   1', end='  ')
        while n_termos > 1:
            termo_atual = ultimo + antes
            antes = ultimo
            ultimo = termo_atual
            print('\033[31m', termo_atual, '\033[m', end=' ')
            n_termos -= 1
            c += 1
            soma.append(termo_atual)
        print('\nesses são os \033[32m{}-ésimos\033[m termos da Fibonacci'.format(c + 1))
        print('A soma dos termos apresentados nessa Fibonacci equivalem a \033[4:36m{}'.format(sum(soma) + 1))

termo = int(input('Digite a quantidade de termos dessa Fibonacci: '))

fibonacci(termo)



