import pandas as pd
import matplotlib.pyplot as plt



data = {
    'Nome': ['João', 'Maria', 'Carlos', 'Ana', 'Pedro', 'Laura', 'Lucas'],
    'Idade': [28, 22, 35, 19, 40, 29, 24],
    'Altura': [175, 163, 180, 158, 190, 168, 175],
    'Peso': [70, 55, 85, 50, 95, 62, 75],
    'Profissão': ['Engenheiro', 'Estudante', 'Advogado', 'Estudante', 'Empresário', 'Médica', 'Designer'],
    'Salário': [8000, 0, 10000, 0, 15000, 9500, 6000],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Recife', 'Porto Alegre', 'Belo Horizonte', 'Brasília']
}


df = pd.DataFrame(data)

print(df.loc[:,'Idade']) #encontra itens por nome, tudo após a virgula é coluna e antes é linha
print()
print(df.iloc[:,1]) #encontra itens por indices, tudo após a virgula é coluna e antes é linha

print(df.columns)

df.plot.bar()
plt.show()
