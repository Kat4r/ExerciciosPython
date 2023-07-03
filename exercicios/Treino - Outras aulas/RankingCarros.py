from modulos.libtestes import testespy as tpy


def arquivarCarros(qtCarros=0, random=False):

    listaCarros = []

    for i in range(qtCarros):
        print(f"Veiculo numero {i+1}")

        try:
            if not random:
                carros = {}
                carros['Veiculo:'] = input("Digite o modelo do veiculo: ").title()
                carros['KM por Litro:'] = float(input("Digite o consumo médio por litro do veiculo: "))
                listaCarros.append(carros)
            else:
                carros = {}
                carros['Veiculo:'] = tpy.carrosRand()
                carros['KM por Litro:'] = float(str(tpy.randint(1,25)) + f".{tpy.randint(1,9)}")
                listaCarros.append(carros)


            with open("Relatorio de Consumo.txt", "a") as relatorio:
                for veiculo, kml in carros.items():
                    relatorio.write(veiculo + str(kml) + "\n")
                if not relatorio.readable():
                    arq = open("Relatorio de Consumo.txt", 'r')



        except Exception as erro:
            print(erro)
            pass
    print("\nLista arquivada com sucesso!\n")
    return listaCarros

def planilhaConsumo(lista, ordenate=False):

    print("="*51)
    print("= posição =", "= veiculo =".center(27), "= consumo =")
    print("=" * 51)
    c = 0

    if not ordenate:
        for pos, conjunto in enumerate(lista):
            print(f"{pos+1}".center(10), end='')
            for carro in conjunto.values():
                c += 1
                if c == 1:
                    print(f"{carro}".center(31), end='')
                else:
                    print(f"{carro}".center(7), end='')
                    c = 0
            print()
    else:
        lista = sorted(lista, key=lambda x: x['KM por Litro:'])
        for pos, carsConj in enumerate(lista):
            print(f"{pos+1}".center(10), end='')
            for carro in carsConj.values():
                c += 1
                if c == 1:
                    print(f"{carro}".center(31), end='')
                else:
                    print(f"{carro}".center(7), end='')
                    c = 0
            print()

quantidade = formato = -1
ordenar = 'e'



while quantidade < 0:
    quantidade = int(input("Quantos veiculos serão adicionados ao mostruário?\n"
                           "\033[32m([ 0 ] Para um valor aleatório entre 1 e 20)\033[m :"))


while formato < 0 or formato >1:
    formato = int(input("\nDeseja informar os carros manualmente ou que sejam gerados de forma aleatoria?\n"
                        "\n[ 0 ] Gerar veiculos aleatórios\n"
                        "[ 1 ] Inserir ambas informações manualmente\n"
                        "\033[32mInsiria aqui: \033[m"))


if quantidade == 0 and formato == 0:
    carros = arquivarCarros(tpy.randint(1,20), random=True)
elif quantidade > 0 and formato == 1:
    carros = arquivarCarros(quantidade)
else:
    carros = arquivarCarros(quantidade, random=True)


while ordenar not in "sSnN":
    ordenar = input("Deseja ordernar a lista do mais economico para o menos economico?: [Sim/Não]").strip()[0]
if ordenar in 'sS':
    planilhaConsumo(carros, ordenate=True)
else:
    planilhaConsumo(carros)










