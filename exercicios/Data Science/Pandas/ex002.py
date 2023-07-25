#pandas boilerplate
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import matplotlib as mpl
mpl.use('TkAgg')
pd.set_option('display.max_colwidth', 30)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
#-----------------------------------
def graficoaltura():

    nbaAlturaPorPontos = pd.pivot_table(nbaPlayers, index='Altura', values=['Pontos', 'Jogos Jogados'])
    nbaAlturaPorPontos.plot.bar()

def show():

    print(f"\nA média de altura dos jogadores é de \033[35m{nbaPlayers['Altura'].mean():.2f} cm\033[m\n"
          f"Maior altura pertence a \033[34m{nomeAlturaMax}\033[m com \033[32m{alturaMax}cm\033[m de altura\n"
          f"Menor altura pertence a \033[34m{nomeAlturaMin}\033[m com \033[31m{alturaMin}cm\033[m de altura\n"
          f"Maior peso encontrado pertence a \033[34m{nomePesoMax}\033[m com \033[32m{pesoMax}Kgs\033[m\n"
          f"Menor peso encontrado pertence a \033[34m{nomePesoMin}\033[m com \033[31m{pesoMin}Kgs\033[m\n"
          f"A escola onde mais teve atletas de basquete foi em \033[33m{nomeEscola}\033[m, com \033[7:47m{contagemEscola[0]} registros\033[m\n"
          f"A Média do IMC dos jogadores é de {nbaPlayers['IMC'].mean():.2f}")

    nome = input('Digite o nome do jogador o qual deseja acessar seu IMC: ').title()
    print(round(float(nbaPlayers[nbaPlayers['Nome  do Jogador'] == f"{nome}"]['IMC'].values[0]), 2))

def alturaPeso():

    plt.figure()
    plt.plot(nbaPlayers['Altura'], nbaPlayers['Peso'], 'ro')
    plt.ylabel('PESO')
    plt.grid()
    plt.show()

def predicao(dado,eixoX,ylabel=None,xlabel=None):

    plt.plot(eixoX, dado.predict(), 'k--')
    plt.ylabel(f"{ylabel}")
    plt.xlabel(f'{xlabel}')
    plt.grid()
    plt.show()


nbaPlayers = pd.read_csv('H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\exercicios\\Data Science\\Datasets\\all_seasons.csv', sep=',')
nbaPlayersBKP = nbaPlayers.copy()

nbaPlayers.rename(columns={'player_name':'Nome do Jogador', 'team_abbreviation':'Abreviação do Time', 'age':'Idade', 'player_height':'Altura',
                           'player_weight':'Peso', 'college':'Escola', 'country':'País', 'draft_year':'Draft da NBA',
                           'draft_round':'Rodada do Draft', 'draft_number':'Numero no Draft', 'gp':'Jogos Jogados',
                           'pts':'Pontos', 'reb':'Rebotes', 'ast':'Assistências', 'net_rating':'Net Rating', 'season':"Temporada"}, inplace=True)

nbaPlayers['Peso'] = nbaPlayers['Peso'].round(2)
IMC = nbaPlayers['IMC'] = nbaPlayers['Peso'] /((nbaPlayers['Altura']/100)**2)
nbaPlayers['Escola'].fillna('Escola não informada', inplace=True)

alturaMax = nbaPlayers['Altura'].max()
nomeAlturaMax = nbaPlayers[nbaPlayers['Altura'] == alturaMax]['Nome do Jogador'].values[0]

alturaMin = nbaPlayers['Altura'].min()
nomeAlturaMin = nbaPlayers[nbaPlayers['Altura'] == alturaMin]['Nome do Jogador'].values[0]

pesoMax = nbaPlayers['Peso'].max()
nomePesoMax = nbaPlayers[nbaPlayers['Peso'] == pesoMax]['Nome do Jogador'].values[0]

pesoMin = nbaPlayers['Peso'].min()
nomePesoMin = nbaPlayers[nbaPlayers['Peso'] == pesoMin]['Nome do Jogador'].values[0]

contagemEscola = nbaPlayers[nbaPlayers['Escola'] != 'Escola não informada']['Escola'].value_counts()
nomeEscola = contagemEscola.index[0]


altura = nbaPlayers['Altura']
peso = nbaPlayers['Peso']
idade = nbaPlayers['Idade']
altIdade = nbaPlayers[['Idade', 'Altura']]
relPesoAltura = sm.OLS(peso,altura).fit()
relIdadeAltura = sm.OLS(idade, altura).fit()
relPesoIdadeAltura = sm.OLS(altIdade,peso).fit()
#predicao(relPesoIdadeAltura,peso,'Relação Idade Altura','PESO')
#predicao(relPesoAltura,altura,'PESO','ALTURA')
#predicao(relIdadeAltura, altura,'IDADE','ALTURA')

print(contagemEscola)
plt.figure(figsize=(12,6))
contagemEscola.head(15).plot.bar(color='purple')
plt.title('Número de inscrições por Escola')
plt.xlabel('Escola')
plt.ylabel('Inscrições')
plt.xticks(rotation=45, ha='center')
plt.tight_layout()
plt.show()

print(nbaPlayers.head())
#nbaPlayers.to_csv('H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\exercicios\\Data Science\\Datasets\\all_seasons.csv', sep=',', index=False)