produtos = ('Smartphone Samsung Galaxy S21 Ultra', 6000,
            'Headphone Sony WH-1000XM4', 3000,
            'Cafeteira Nespresso Inissia', 499,
            'Televisor LG OLED CX 65"', 15000,
            'Console de videogame Xbox Series X', 5000,
            'Notebook Lenovo IdeaPad 5', 4900,
            'Câmera Canon EOS Rebel T7i', 3300,
            'Geladeira Brastemp Frost Free', 3700,
            'Tênis Nike Air Max 2090', 750,
            'Bicicleta Caloi Elite Carbon Sport', 15800)

print('\033[7:38m---------------------------------------------------------------\033[m\n'
      '\033[7:38m-------------------------Lojão das 7---------------------------\033[m\n'
      '\033[7:38m---------------------------------------------------------------\033[m')

for produto in range(0, len(produtos),2):
    print(f'\033[34m{produtos[produto]:.<50}\033[m \033[32mR${produtos[produto+1]:>10.2f}\033[m')
print('\033[7:38m---------------------------------------------------------------\033[m')



