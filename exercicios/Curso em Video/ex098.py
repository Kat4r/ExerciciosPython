import time

def contador(start,stop,step):

    if start < stop:
        for i in range(start,stop+1,step):
            print(i, end=" ")
            time.sleep(0.1)
        print("FIM!")
    else:
        step = step * -1
        for i in range(start,stop-1,step):
            print(i, end=" ")
            time.sleep(0.1)
        print("FIM!")


contador(1,10,1)
contador(10,0,1)

print("Agora é sua vez!")
start = int(input("digite o inicio: "))
stop = int(input("Digite o fim: "))
step = abs(int(input("Digite o passo \033[33m[ 1 ] para começar do 0\033[m:  ")))

contador(start,stop,step)



