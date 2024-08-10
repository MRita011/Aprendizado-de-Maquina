import pandas as pd

# Carregar os dados do arquivo CSV
voos = pd.read_csv('./MODULO1/data/aulas/juncao_tabelas/voos.csv', delimiter=';')

# Mostrar as primeiras linhas do DataFrame
print('Voos')
print(voos.head())
print('\n')

# Verificar os tipos de dados das colunas
print('Tipos de dados das colunas:')
print(voos.dtypes)
print('\n')

# Tabela pivô (com a média de passageiros por ano e mês)
pivot = pd.pivot_table(voos, index=['year', 'month'], values='passengers', aggfunc='mean')
print('Tabela Pivô (ano, mês)')
print(pivot)
print('\n')

# Tabela pivô (com a média de passageiros por mês e ano)
pivot = pd.pivot_table(voos, index=['month', 'year'], values='passengers', aggfunc='mean')
print('Tabela Pivô (mês, ano)')
print(pivot)
print('\n')

# Agrupando dados por ano
print('Voos por ano')
voos_por_ano = voos.groupby('year')
print(voos_por_ano.describe())
print('\n')

# Buscando informações isoladas
print('Quantidade máxima (passageiros) por ano')
info = voos_por_ano['passengers'].max()
print(info)
print('\n')

print('Média de passageiros por ano')
info = voos_por_ano['passengers'].mean()
print(info)
print('\n')

# Agrupando dados por mês
print('Voos por mês')
voos_por_mes = voos.groupby('month')
print(voos_por_mes.describe())
print('\n')

# Média dos passageiros por mês
media_voos_por_mes = voos_por_mes['passengers'].mean()
print('Média de passageiros por mês')
print(media_voos_por_mes)
print('\n')

# Utilizando o transpose (meses e anos em colunas)
# !! transpose é muito utilizado em sistemas de recomendações !!
print('Anos e Meses (transpose)')
pivot = pd.pivot_table(voos, index=['year', 'month']).transpose()
print(pivot)
print('\n')

print('Voos (transpose)')
print(voos.transpose())
print('\n')