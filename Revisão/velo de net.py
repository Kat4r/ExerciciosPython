aqv = float(input('Digite o tamanho: '))
mbps = float(input('Velocidade da internet: '))
aqvmb = aqv * 1000
veloreal = mbps / 8
tseg = aqvmb / veloreal
tmin = tseg / 60
thora = tmin / 60
print('seu arquivo de {}MB irá demorar em média {:.2f} minutos ou {:.2f} horas para a conclusão'.format(aqv,tmin,thora ))





"""Faça um programa que peça o tamanho de um 
arquivo para download (em MB) e a velocidade de um link de Internet 
(em Mbps), calcule e informe o tempo aproximado 
de download do arquivo usando este link (em minutos)."""