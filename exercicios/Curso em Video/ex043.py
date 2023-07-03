peso = float(input('Qual seu peso?(Kg): '))
altura = float(input('Digite sua altura (cm): '))
imc = (peso / (altura * altura)) * 10000
if imc <= 18.5:
    print('\033[36mVocê está abaixo do peso!!')
elif imc <= 24.9:
    print('\033[32mVocê está no peso ideal!')
elif imc <= 29.9:
    print('\033[34mVocê está acima do peso, tome cuidado!')
elif imc <= 34.9:
    print('\033[31mVocê está acima do peso, Obesidade de grau 1!')
elif imc <= 39.9:
    print('\033[31mVocê está acima do peso, Obesidade de grau 2!')
else:
    print('q isso em thais carla 🥵🥵🥵🥵')
print(f'Seu imc é de: {imc:.2f}')
