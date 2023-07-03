import time

def maior(* num):
    print(f"\033[34mAnalisando valores. . . \n"
          f"\033[31m{', '.join(map(str, num))}\033[m foram os valores informados, ao todo foram informados \033[31m{len(num)}\033[m numeros.\n"
          f"O maior numero foi \033[32m{max(num)}\033[m, e o total dos numeros somados foi \033[32m{sum(num)}\033[m\n")


maior(4,9,5,2,1,7,9)