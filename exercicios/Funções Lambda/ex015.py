pessoas = [
    {'Nome': 'Vincius','Idade': 23},
    {'Nome': 'Matheus','Idade': 32},
    {'Nome': 'Sonic','Idade': 25},
    {'Nome': 'PT','Idade': 14},
    {'Nome': 'PAM','Idade': 90},
    {'Nome': 'Pachiega','Idade': 72},
]


itensdict = lambda lista: sorted(lista, key=lambda pessoa: pessoa['Idade'])

print(itensdict(pessoas))


#vencedores = sorted(jogadores.items(), key=lambda x:x[1], reverse=True)