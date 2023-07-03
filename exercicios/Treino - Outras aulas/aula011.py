nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')
for errado in senha:
    if senha == nome:
        print('A senha não pode ser igual ao nome')
        senha = input('Digite outra senha: ')
print('Usuario cadastrado!')

################################

nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')
while senha == nome:
    print('A senha não pode ser igual ao nome')
    senha = input('Digite outra senha: ')
print('Usuario cadastrado!')

