casa = int(input("Digite o valor da casa R$"))
sal = int(input('Digite o seu salario R$'))
ano = int(input('Em quantos anos deseja pagar? '))
dsal = (sal * 30) / 100
emprestimo = casa / (ano * 12)
if  emprestimo < dsal:
    print('Emprestimo \033[1:32mAPROVADO!\033[m baseado em 30% do seu salario equivalente a {} '.format(dsal))
else:
    print('Emprestimo \033[1:31mNEGADO!\033[m baseado em 30% do seu salario equivalente a {} '.format(dsal))
