
senha = open('../senhas.txt', 'r')
senha = senha.readlines()
arraySenhas = []
valoresSenhas = []


for linhas in senha:
    arraySenhas.append(linhas)
print(arraySenhas)

for item in arraySenhas:
    tamSenha = len(item)
    valoresSenhas.append(tamSenha)
    print(tamSenha, end=' ')


divisor = len(valoresSenhas)      #divide pelo tanto de item na lista
divSenhas = sum(valoresSenhas) / divisor    #resultado da divisão











