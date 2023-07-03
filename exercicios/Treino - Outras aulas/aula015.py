pa = str(input('Digite 2 numeros com um \033[34mESPAÇO\033[m entre eles'
               '\nConseidere o primeiro digito para  \033[1:32mINICIO\033[m e o segundo para \033[1:32mRAZÃO\033[m: ')).split()
pa_int = [int(num)for num in pa]
for pr in range(pa_int[0],pa_int[1] * 11,pa_int[1]):
    print(' -> ',pr, end='')
print('FIM!')


