#pandas boilerplate
import pandas as pd
pd.set_option('display.max_colwidth', 30)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
#-----------------------------------

nbaPlayers = pd.read_csv('H:\\Meus Códigos\\paito\\ai ui ai ui q dor\\exercicios\\Data Science\\Datasets\\all_seasons.csv', sep=',')
nbaPlayersBKP = nbaPlayers.copy()

nbaPlayers = nbaPlayers.rename(columns={'player_name':'Nome do Jogador', 'team_abbreviation':'Abreviação do Time', 'age':'Idade', 'player_height':'Altura',
                           'player_weight':'Peso', 'college':'Escola', 'country':'País', 'draft_year':'Draft da NBA',
                           'draft_round':'Rodada do Draft', 'draft_number':'Numero no Draft', 'gp':'Jogos Jogados',
                           'pts':'Pontos', 'reb':'Rebotes', 'ast':'Assistências', 'net_rating':'Net Rating'})


print(nbaPlayers.head())

