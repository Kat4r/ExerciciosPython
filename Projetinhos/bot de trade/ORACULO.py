
import random
import datetime
mes = datetime.date.today().month
dia = datetime.date.today().day
agora = datetime.datetime.now()
hora = agora.hour
minuto = agora.minute


velas = ['M1','M5','M10','M15']
metodo = ['Venda','Compra']
paresInt, paresSoltos = [], []



with open('pares de moedas.txt') as paresMoedas:
    for item in paresMoedas:
        paresInt.append(item)
for par in paresInt:
    individual = par.strip()
    paresSoltos.append(par[0:7])

def trade():

    tempoH = random.randint(00, 23)
    tempoM = random.randint(00, 59)
    while tempoH < hora:
        tempoH = random.randint(00, 23)
    while tempoM <= hora:
        tempoM = random.randint(00, 59)

    metodo2 = {random.choice(metodo)}
    velasUso = random.choice(velas)
    if len(velasUso) == 2:
        velasUso += ' '
    print('\033[34m',random.choice(paresSoltos),'\033[m',velasUso , end='')
    if 'Venda' in metodo2:
        print('\033[31m Venda  \033[m', end='')
    elif 'Compra' in metodo2:
        print('\033[32m Compra \033[m', end='')

    print('{:02d}:{:02d}  \033[34m{}\033[m'.format(tempoH, tempoM, ('Data: {:02d}/{:02d}'.format(dia, mes))))

for i in range(0,100):
    trade()
trade()




