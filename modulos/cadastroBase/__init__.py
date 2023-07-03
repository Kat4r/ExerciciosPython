def intro(num):
    frase = f"Opção {num}".center(42)
    print('-' * len(frase))
    print(frase)
    print('-' * len(frase))

def menu(lista):
    print("\033[4mEscolha uma das opções a seguir\033[m\n".center(48))
    for pos, item in enumerate(lista):
        print(f"\t\033[3{pos+1}m[ {pos+1} ]\033[m  {item}")

def cadastro(nome, idade, arquivo=''):

    while not idade.isdigit():
        idade = input("Digite somente numeros: ")
    with open(arquivo, "a", encoding="UTF-8") as arq:
        arq.write(f"\nNome: {nome}\nIdade: {idade}")

def mostrarCadastro(arquivo):
    with open(arquivo, "r", encoding="utf-8") as arq:
        for linha in arq.readlines():
            if linha.startswith("Nome: "):
                print(f"{linha.strip():<32}", end='')
            elif linha.startswith("Idade: "):
                print(f"{linha.strip():}")
def abertura():
    frase = "Menu Principal".center(42)
    print("-" *len(frase))
    print(frase)
    print("-" *len(frase))
