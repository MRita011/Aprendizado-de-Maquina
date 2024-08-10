# Imports
import pandas as pd 

# Lê o arquivo CSV 'temperaturas.csv' localizado no diretório especificado, usando ';' como delimitador
tabela = pd.read_csv('./MODULO1/data/aulas/temperaturas.csv', delimiter=';')

# Exibe as primeiras 7 linhas da tabela
print(tabela.head(7))
print("\n")

# Lê o mesmo arquivo CSV, mas desta vez define a coluna 'dia' como o índice
tabela = pd.read_csv('./MODULO1/data/aulas/temperaturas.csv', delimiter=';', index_col=['dia'])

# Exibe as primeiras 7 linhas da tabela com a coluna 'dia' como índice
print(tabela.head(7))
print("\n")

# Acessa o valor da coluna 'temperatura' na linha onde o índice é 'sex' (sexta-feira)
print(tabela.loc['sex', 'temperatura'])
print("\n")

# Define listas de dias e informações para serem usadas em seleções subsequentes
dias = ['seg', 'qui', 'dom']
infor = ['clima', 'vento', 'temperatura']

# Selec. as linhas correspondentes aos dias especificados e as colunas especificadas
print(tabela.loc[dias, infor])
print("\n")

# Selec. todas as colunas para as linhas correspondentes aos dias especificados
print(tabela.loc[dias, :])
print("\n")

# Selec. as colunas 'vento' e 'temperatura' para as linhas que vão de 'ter' (terça-feira) a 'sab' (sábado)
print(tabela.loc['ter':'sab', ['vento', 'temperatura']])
print("\n")

# Selec.as colunas 'vento' e 'temperatura' para as linhas que vão de 'ter' (terça-feira) a 'sex' (sexta-feira)
print(tabela.loc['ter':'sex', ['vento', 'temperatura']])
print("\n")

# Selec. todas as colunas para as linhas onde a umidade é maior que 50
print(tabela.loc[tabela.umidade > 50, :])
print("\n")

# Selec. a coluna 'clima' para as linhas onde a umidade é maior que 50
print(tabela.loc[tabela.umidade > 50, ['clima']])
print("\n")

# Selec. todas as colunas para as linhas onde a umidade é maior que 50 e o clima é 'chuva'
print(tabela.loc[(tabela.umidade > 50) & (tabela.clima == 'chuva'), :])
print("\n")

# (Duplicado) Selec. todas as colunas para as linhas onde a umidade é maior que 50 e o clima é 'chuva'
print(tabela.loc[(tabela.umidade > 50) & (tabela.clima == 'chuva'), :])
print("\n")

# Selec. todas as colunas para as linhas onde a umidade é maior que 50 ou o clima é 'nublado'
print(tabela.loc[(tabela.umidade > 50) | (tabela.clima == 'nublado'), :])