import mysql.connector

dados = mysql.connector.connect(user='root',password='71433969',host='127.0.0.1')
dadosexp = dados.cursor()

arq1 = open("array de ingredientes.txt")
arq2 = open('array de lanches prontos.txt')
ingredientes = str(arq1.readline()).split()
lanches_prontos = str(arq2.readline()).split()
print(ingredientes,"\n",lanches_prontos)

dados.close()
