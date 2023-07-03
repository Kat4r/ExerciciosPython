ph = float(input('Quanto vc ganha por hora? '))
tpm = float(input('Quanto vc trabalha em um mes? '))
sal = gph*tpm
ir = (11 * sal)/100
inss = (8 * sal)/100
sind = (5 * sal)/100
sal2 = sal - (ir + inss + sind)
print('Voce recebe R${} ao mes, R${:.2f} irá ao INSS e R${:.2f} ao Sindicato. \nPortanto seu salario liquido será de R${:.2f}'.format(sal,inss,sind,sal2))






"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""