import pandas as pd
import numpy as np

lista1 = [1,2,3]
lista2 = ['a','b','c']

listaUnida = pd.Series(lista2, index=lista1) #cria uma serie, o index é totalmente opcional

dic = {'Impares':np.arange(1,21,2), 'Pares':np.arange(2,22,2), 'Sequencial':np.arange(1,11)} #criando uma estrutura de dataframe
df = pd.DataFrame(dic)
print(df)
