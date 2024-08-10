# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv('./MODULO1/data/aulas/titanic.csv', delimiter=';')
df = sns.load_dataset('titanic')

print('Titanic\n-------')
print(df.head())
print('\n')

# Contagem dos valores únicos na coluna 'sex'
print('Contagem por sexo\n----------------')
print(df['sex'].value_counts())
print('\n')

# Contagem dos valores únicos na coluna 'embark_town'
print('Contagem por cidade de embarque\n------------------------------')
print(df['embark_town'].value_counts())
print('\n')

# Informações gerais sobre o dataframe Titanic
print('Informações gerais\n----------------')
print(df.info())
print('\n')

# Estatísticas descritivas do dataframe Titanic
print('Estatísticas descritivas\n-----------------------')
print(df.describe())
print('\n')

# Verificação de valores nulos no dataframe Titanic
print('Verificação de valores nulos\n--------------------------')
print(df.isnull())
print('\n')

# Verificação de colunas com valores nulos no dataframe Titanic
print('Colunas com valores nulos\n--------------------------')
print(df.isnull().any())
print('\n')

# Heatmap dos valores nulos no dataframe Titanic
print('Mapa de calor dos valores nulos\n----------------------------')
sns.heatmap(df.isnull())
plt.show()
print('\n')

# Carregando o dataset Iris do Seaborn
df = sns.load_dataset('iris')

# Seleção das colunas numéricas para calcular a correlação
numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

print('Iris\n----')
print(df.head())
print('\n')

# Função para calcular o quadrado de um número
def quadrado(x):
    return x * x

# Aplicando a função quadrado na coluna 'sepal_length'
print('Quadrado do comprimento da sépala\n---------------------------------')
print(df['sepal_length'].apply(quadrado))
print('\n')

print('Iris após aplicação da função quadrado\n--------------------------------------')
print(df.head())
print('\n')

# Aplicando uma função lambda na coluna 'sepal_length'
df['sepal_length'] = df['sepal_length'].apply(lambda x: x * x)
print('Iris após aplicação da função lambda\n--------------------------------------')
print(df.head())
print('\n')

# Ordenação do dataframe Iris pela coluna 'petal_width'
print('Iris ordenado por largura da pétala\n----------------------------------')
print(df.sort_values(by='petal_width'))
print('\n')

# Ordenação do dataframe Iris pelas colunas 'petal_width' e 'petal_length'
print('Iris ordenado por largura e comprimento da pétala\n-------------------------------------------')
print(df.sort_values(by=['petal_width', 'petal_length']))
print('\n')