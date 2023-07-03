listaSenhas = []
valorSenha = []
import string
import  math
with open('teste de senhas.txt','r+') as arquivo:
    for linhas in arquivo:
        listaSenhas.append(linhas)
    for item in listaSenhas:
        tamSenha = len(item)
        item = item.strip()
        valorSenha.append(tamSenha)

senhateste = listaSenhas[0].strip()
c_upper = c_lower = c_digito = c_simbolo = 0
for letra in senhateste:
    if letra.isupper() == True:
        c_upper += 1
    elif letra.islower() == True:
        c_lower += 1
    elif letra.isdigit() == True:
        c_digito += 1
    elif letra.isascii() == True:
        c_simbolo += 1
cracker =''
if c_simbolo > 0 and c_digito > 0 and c_lower > 0 and c_upper > 0:
    cracker = string.printable + string.digits
elif c_lower > 0 and c_upper > 0 and c_digito == 0:
    cracker = string.ascii_letters + string.digits
elif c_lower > 0 and c_upper > 0 and c_simbolo > 0:
    cracker = string.ascii_letters + string.punctuation
print(c_upper,c_lower,c_digito,c_simbolo)
print(cracker)

media = len(valorSenha)
menorSenha = max(valorSenha)
maiorSenha = min(valorSenha)
mediaSenha = math.trunc(sum(valorSenha) / media)








