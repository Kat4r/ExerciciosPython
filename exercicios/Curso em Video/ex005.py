n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
soma = n1 + n2
ant = soma - 1
suc = soma + 1
print('a somatoria de \033[1:33m{}\033[m com \033[1:33m{}\033[m resulta em \033[32m{}\033[m, tendo seu antecessor em \033[1:31m{}\033[m e seu sucessor em \033[1:32m{}\033[m'.format(n1,n2,soma,ant,suc))