
produtos = []
menorValor = float('inf')
print('\033[7:31m-'*30,'\033[m')
print('\033[7:34m        Casas Sudeste         ','\033[m')
print('\033[7:34m-'*30,'\033[m')
cont = 0

while True:
    nomeProd = str(input('Qual o produto? ')).strip().title()
    valorProd = float(input('Digite o preço do produto R$'))
    if valorProd < menorValor:
        menorValor = valorProd
        prodBarato = nomeProd
    if valorProd >= 1000:
        cont += 1
    produtos.append(valorProd)

    pausa = str(input('Digite "P" para encerrar: ')).strip().lower()[0]
    if pausa == 'p':
        break

print(f'Foi gasto um total de {sum(produtos)} na compra\n'
      f'{cont} produtos custaram mais de R$1000\n'
      f'e o produto mais barato foi {prodBarato} custando apenas {menorValor}')
