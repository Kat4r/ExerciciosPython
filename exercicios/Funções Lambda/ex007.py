pessoas = [
    {'Nome': 'Vincius','Idade': 23},
    {'Nome': 'Matheus','Idade': 32},
    {'Nome': 'Sonic','Idade': 25},
    {'Nome': 'PT','Idade': 14},
    {'Nome': 'PAM','Idade': 90},
]

ordIdade = lambda lista: sorted([idade['Idade'] for idade in lista])
print(ordIdade(pessoas))
