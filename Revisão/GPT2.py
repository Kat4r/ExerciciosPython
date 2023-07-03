frutas = ["maçã", "banana", "laranja", "manga", "uva", "abacaxi", "melancia", "pêssego", "kiwi", "morango"]

escolha = input('Adicione uma fruta nova: ').strip().lower()

#um loop é criado para decorrer cada uma das frutas dentro da lista
for fruta in frutas:
    #um while é iniciado para testar se a fruta a ser adicionada é igual a cada uma das frutas iteradas
    while escolha == fruta.strip():
        escolha = input('Já temos essa fruta adicionada!\n'
                        'tente outra!: ').strip().lower()
print(f"A fruta \033[31m{escolha.title()}\033[m foi adicionada!")
