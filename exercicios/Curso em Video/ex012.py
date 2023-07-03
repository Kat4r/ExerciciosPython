preco = int(input('Digite o valor do produto: '))
desconto = (preco / 100) * 5
valFinal = preco - desconto
print(f'O valor final já com o desconto de 5% será \033[32mR${valFinal:.2f}')

