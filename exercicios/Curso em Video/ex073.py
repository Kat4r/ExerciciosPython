import  random as r
timesLista = []
cores = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', ]

with open('../../modulos/libtestes/times.txt', 'r', encoding='UTF-8') as times:
    for time in times:
        timesLista.append(time.strip().title())
r.shuffle(timesLista)

timeEscolhido = str(input('Escolha um time: ')).title()
escolha = timesLista.index(timeEscolhido)
ord = ', '.join(timesLista)

print(f'Times do Brasileirão!\n'
      f'========================\n'
      f'Ordem dos vencedores: \033[34m{ord}\033[m')
print('Os 3 primeiros vencedores são:\033[32m {}\033[m'.format(', '.join(timesLista[:3])))
print('Os 3 ultimos colocados são:\033[32m {}\033[m'.format(', '.join(timesLista[-3:])))
print('Os times em ordem alfabética serão:\033[32m {}\033[m'.format(', '.join(sorted(timesLista))))
print(f'O time \033[31m{timeEscolhido}\033[m está em {escolha}* lugar. ')



