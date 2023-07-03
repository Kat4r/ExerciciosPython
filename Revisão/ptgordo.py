from modulos.libtestes import  testespy as tpy

pessoaGorda = pessoaLeve = resp = ''
massa, dados = [],[]
while resp != 'n':
    pessoas = {}                                             #cria um dicionario novo sempre que o loop der uma volta
    nome = input("Digite seu NOME: ").strip()
    while not nome.isalpha():
        nome = input('Digite somente letras em seu NOME: ').strip() #verifica se o input é somente letras
    pessoas['Nome'] = nome
    while True:
        try:
            peso = tpy.idadeRand()  #também tem a verificação se é um número ou letra. (porém com Try)
            massa.append(peso)
            break
        except:
            print("O peso digitado é invalido.")
            continue
    resp = input('Quer continuar? [S/N] ').lower()[0]
    dados.append(pessoas)
pessoas['Peso'] = massa


print(f'Foram cadastrados {len(dados)} pessoas.')
print(f"maior: {max(massa)}, menor: {min(massa)}\n"
      f"O maior peso cadastrado foi {max(massa)} pertencente à: {dados[tpy.encontrarMassa(massa, gordo=True)]['Nome']}\n"
      f"O menor peso cadastrado foi {min(massa)} pertence à: {dados[tpy.encontrarMassa(massa)]['Nome']}")
