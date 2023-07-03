c = contagem = 0
escolha = 10
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão dessa PA: '))
while escolha != 0:
    contagem = contagem + escolha
    c = 0
    while c <= escolha:
        termo = termo + razao
        print(termo, '-> ', end="")
        c = c + 1
    print('Fim', end='')
    escolha = int(input('\nQuantos termos deseja exibir? '))
print('\033[32m Fim dessa PA, foram contados {} termos'.format(contagem))#startstopstep ftw
