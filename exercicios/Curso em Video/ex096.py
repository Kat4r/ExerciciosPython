def areaquadrada(largura, comprimento):
    print(f"\nA area com os valores informados equivalem a: \033[32m{largura * comprimento}m²")


print("     Área     \n"
      "--------------")
areaquadrada(float(input("Largura(m): ")),float(input("Comprimento(m): ")))

