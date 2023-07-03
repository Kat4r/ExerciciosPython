loop = True
numeros = []
print('\033[1:31:43m~'*45,'\033[m')
print('\033[7:48m  Calculadora automatica, digite 0 para sair  \033[m')
print('\033[1:31:43m~'*45,'\033[m')
num = ''
while num !=0:
    num = float(input('Digite um numero: '))
    numeros.append(num)
numeros.pop(-1)
str_num = ' + '.join(map(str, numeros))
print(str_num, end='')
print(' =\033[32m', sum(numeros))



