c = csem = 0

expnum = str(input('Digite uma expressão numérica: '))

for parenteses in expnum:
    if "(" in parenteses:
        c = c + 1

for parenteses in expnum:
    if ')' in parenteses:
        csem = csem + 1


if c == csem:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')


####################################

expnum = str(input('Digite uma expressão numérica: '))
parenteses = []
for simbolo in expnum:
    if simbolo == '(':
        parenteses.append(simbolo)
    elif simbolo == ')':
        if len(parenteses) >0:
            parenteses.pop()
        else:
            parenteses.append(')')
if len(parenteses) != 0:
    print('A expressão é inválida!')
else:
    print('A expressão é válida!')
