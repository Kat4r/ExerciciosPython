nomes = ('ana','roberto','vinicius','claudia','larissa','abelardo','juta')

for quantia, nome in enumerate(nomes):
    if 'a' in nome:
        print(nome, end='')
        if quantia < len(nomes) - 2:
            print(', ', end='')
        elif quantia == len(nomes) - 2:
            print(' e ', end='')
print('.')
