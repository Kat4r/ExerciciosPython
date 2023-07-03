arq1 = open('projeção de vida.txt')
txt = str(arq1.read())
txt_bin = ' '.join(format(ord(c), 'b') for c in txt)
print(txt_bin)


