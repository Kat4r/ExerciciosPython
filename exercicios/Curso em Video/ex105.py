def analisarNotas(*n,situacao=True):
    """
    -> func para calcular media de alunos e mostrar na tela
    :param n: notas, pode por quantas quiser
    :param situacao: mostra a situação atual do aluno sabendo que >= 5 é aprovado, e abaixo é reprovado
    :return: retorna os valores escolares incluindo sua média, total, maior nota e menor
    """

    escola = {}
    escola['Total'] = len(n)
    escola['Maior'] = max(n)
    escola['Menor'] = min(n)
    escola['Média'] = float(f'{sum(n) / len(n):.2f}')

    if situacao:
        if escola['Média'] >= 5:
            resultado = '\033[32mAprovado\033[32m'
        else:
            resultado = '\033[31mReprovado\033[31m'
        escola['Situação'] = resultado

    for k,v in escola.items():
        print(f"{k} : {v:}")

    return escola

analisarNotas()
