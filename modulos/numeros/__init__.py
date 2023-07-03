
def dobro(num, moeda=False):
    return num * 2 if moeda is False else formatarnum(num * 2)

def metade(num, moeda=False):
    return f"{num /2:.2f}" if moeda is False else formatarnum(f"{num /2:.2f}")

def aumento(num, valorAumento, moeda=False):
    soma = (num * valorAumento) / 100
    return int(soma + num) if not moeda else formatarnum(int(soma + num))

def decrescimo(num, valorReduzido, moeda=False):
    soma = (num * valorReduzido) / 100
    return int(num - soma) if not moeda else formatarnum(int(num - soma))

def formatarnum(num):
    numstr = str(num)
    if '.' in numstr:
        return "R$" + numstr.replace(".", ",")
    else:
        return "R$" + numstr + ",00"

def resumo(preco,aum,redu, moeda=False):

    while not preco.isdigit():
        if "," in preco or "." in preco:
            preco = preco.replace(",", ".")
            break
        else:
            print(f"\033[31m{preco}\033[m não é um valor")
            preco = input("Digite o valor R$")

    preco = float(preco)


    print(f"o dobro de {preco} é: \t\t{dobro(preco) if not moeda else dobro(preco, True)}\n"
          f"a metade de {preco} é: \t\t{metade(preco) if moeda is False else metade(preco, True)}\n"
          f"{preco} aumentado em {aum}% é: \t{aumento(preco,aum) if not moeda else aumento(preco, aum, True)}\n"
          f"{preco} reduzido em {redu}% é: \t{decrescimo(preco, redu) if moeda is False else decrescimo(preco, redu, True)}")
