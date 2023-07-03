def leiaint():
    while True:
        try:
            num = int(input("Digite um numero inteiro: "))
        except:
            print("\033[31mERRO: Digite apenas numeros validos!!\033[m")
            pass
        else:
            return num

def leiaReal():
    while True:
        try:
            num2 = input("Digite um numero real: ")
            while '.' not in num2:
                num2 = input("Digite um numero real: ")
            num2 = float(num2)
        except:
            print("\033[31mERRO: Digite apenas numeros validos!!\033[m")
            pass

        else:
            return num2



inteiro = leiaint()
real = leiaReal()


print(f"Os numeros informados foram: {inteiro} inteiro e: {real} real")

