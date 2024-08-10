# Imports
import pandas as pd

titanic = pd.read_csv('./MODULO1/data/aulas/titanic.csv', delimiter=';')

print('Titanic\n-------')
print(titanic.head())
print('\n')

# Exibindo a coluna 'sex' do dataframe Titanic
print('Gênero dos passageiros\n-----------------------')
print(titanic.sex)
print('\n')

# Convertendo a coluna 'sex' em variáveis dummy
sexoPassageiros = pd.get_dummies(titanic.sex)
print('Gênero dos passageiros (nova tabela)\n------------------------------------')
print(sexoPassageiros)
print('\n')

# Adicionando as colunas dummy ao dataframe Titanic
titanic[['female', 'male']] = pd.get_dummies(titanic.sex)
print('DataFrame com colunas dummy adicionadas\n--------------------------------------')
print(titanic.head())
print('\n')

# Removendo a coluna 'sex' original do dataframe Titanic
titanic.drop(['sex'], axis=1, inplace=True)
print('DataFrame após remoção da coluna "sex"\n------------------------------------')
print(titanic.head())
print('\n')

# Removendo a coluna 'male' do dataframe Titanic
titanic.drop(['male'], axis=1, inplace=True)
print('DataFrame após remoção da coluna "male"\n------------------------------------')
print(titanic.head())
print('\n')

# Filtrando e removendo inconsistências no dataframe Titanic
titanic = titanic.loc[~(((titanic.female == 0) & (titanic.who == 'woman')) | ((titanic.female == 1) & (titanic.who == 'man')))]
titanic = titanic.loc[~(((titanic.survived == 0) & (titanic.alive == 'yes')) | ((titanic.survived == 1) & (titanic.alive == 'no')))]

# Removendo as colunas 'who' e 'alive'
titanic.drop(['who', 'alive'], axis=1, inplace=True)
print('DataFrame após remoção das colunas "who" e "alive"\n------------------------------------------')
print(titanic.head())
print('\n')

# Convertendo a coluna 'embark_town' em variáveis dummy
embark_dummies = pd.get_dummies(titanic.embark_town)

# Adicionando colunas dummy ao dataframe Titanic, exceto 'Cherbourg'
titanic[['Queenstown', 'Southampton']] = embark_dummies.drop(['Cherbourg'], axis=1)

# Removendo a coluna 'embark_town' original do dataframe Titanic
titanic.drop(['embark_town'], axis=1, inplace=True)
print('DataFrame após remoção da coluna "embark_town" e adição das dummies\n------------------------------------------')
print(titanic.head())
print('\n')