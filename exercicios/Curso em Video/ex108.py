import modulos.numeros as nmr

valor = int(input("Digite um numero qualquer: "))
aumento = int(input("Valor do aumento: "))

print(f"O dobro de {valor} é {nmr.dobro(valor)}\n"
      f"A metade de {valor} é {nmr.metade(valor)}\n"
      f"{valor} aumentado em {aumento}% é {nmr.aumento(valor, aumento, True)}\n"
      f"{valor} reduzido em {aumento}% é {nmr.decrescimo(valor, aumento, True)} ")