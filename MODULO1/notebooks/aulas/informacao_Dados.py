# Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados
titanic = pd.read_csv('./MODULO1/data/aulas/titanic.csv', delimiter=';')

# Exibindo os primeiros dados do DataFrame
print('Titanic\n-------')
print(titanic.head())
print('\n')

# Contando os sobreviventes
print('Sobreviventes\n-------------')
sobreviventes = titanic.survived.value_counts()
print(sobreviventes)
print('\n')

# Contando as cidades que foram mais embarcadas
print('Cidades mais embarcadas\n-----------------------')
cid_embarcadas = titanic.embark_town.value_counts()
print(cid_embarcadas)
print('\n')

# Overview sobre todo o conjunto de informações
print(titanic.info())
print('\n')

# Descrevendo os dados (numéricos)
print('Describe\n-------')
print(titanic.describe())
print('\n')

# Averiguando quais valores faltam na tabela original
print(titanic.isnull().sum())
print('\n')

# Verificando se há qualquer valor nulo
print(titanic.isnull().any())
print('\n')

# Corrigindo o erro de digitação
print('Colunas\n-------')
print(titanic.columns)
print('\n')

# Convertendo colunas 'age' e 'fare' para o formato numérico correto
titanic['age'] = titanic['age'].str.replace(',', '.').astype(float)
titanic['fare'] = titanic['fare'].str.replace(',', '.').astype(float)

# Selecionando colunas numéricas e calculando a correlação
numeric_cols = ['age', 'fare', 'pclass', 'survived']
correlation_matrix = titanic[numeric_cols].corr()
print('Matriz de Correlação\n-------------------')
print(correlation_matrix)
print('\n')

# 1: Correlação perfeita positiva. Quando uma variável aumenta, a outra também aumenta proporcionalmente
# 0: Nenhuma correlação linear. As variáveis não têm relação linear
# -1: Correlação perfeita negativa. Quando uma variável aumenta, a outra diminui proporcionalmente

# Visualizando a matriz de correlação
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlação')
plt.show()

# Criando o heatmap para valores nulos (riscos claros)
print('Heatmap\n-------')
plt.figure(figsize=(10, 6))
sns.heatmap(titanic.isnull(), cbar=True, cmap='magma', yticklabels=False)
plt.show()
