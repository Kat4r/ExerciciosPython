s = 0
cont = 0
for num in range(1,500,2):
    if num % 3 == 0:
        s = s + num
        cont = cont + 1
print('A soma de todos os {} numeros é igual a {}'.format(cont,s))
