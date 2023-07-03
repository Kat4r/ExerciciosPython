import random

itens = list(range(1,101)) #lista ordenada

#itens = []
#for i in range(1,100): #lista desordenada
    #itens.append(random.randint(1,101))

menorNum = 0
ordernado = True
for pos,item in enumerate(itens):
    if pos == 0:
        menorNum = item
    if item >= menorNum:
        menorNum = item
        continue
    else:
        print("Execução interrompida, a lista está desordenada")
        print(f"o item a seguir é {item} e o passado é {menorNum}")
        ordernado = False
        break
if ordernado:
    print("A lista está ordenada")


meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mesReq = int(input("Digite um numero: "))-1
while mesReq < 0 or mesReq > 11:
    mesReq = int(input("há somente 12 meses, digite apenas valores entre 1 e 12: "))-1

print(meses[mesReq])
