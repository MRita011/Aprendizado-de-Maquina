import pandas as pd

# Carrega o arquivo CSV
tabela = pd.read_csv('./MODULO1/data/aulas/Matriculados.csv', delimiter=';')

# Exibe as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:\n")
print(tabela.head())
print("\n")  # Adiciona uma linha em branco para separação

# Acessa a coluna 'nome'
print("Coluna 'nome':\n")
print(tabela['nome'])
print("\n")

# Define as colunas a serem selecionadas
colunas = ['nome', 'peso']
print("Colunas selecionadas:\n")
print(colunas)
print("\n")

# Exibe as colunas selecionadas do DataFrame
print("Colunas selecionadas do DataFrame:\n")
print(tabela[colunas])
print("\n")

# Exibe diferentes fatias do DataFrame
print("Todos os dados do DataFrame:\n")
print(tabela.iloc[:,:])
print("\n")

print("Dados do DataFrame, a partir da linha 1:\n")
print(tabela.iloc[1:,:])
print("\n")

print("Dados do DataFrame, da linha 1 até 2:\n")
print(tabela.iloc[1:3,:])
print("\n")

# Define uma lista de valores para adicionar como uma nova coluna
n_filhos = [0, 0, 2, 1]
print("Lista de número de filhos:\n")
print(n_filhos)
print("\n")

# Adiciona a nova coluna ao DataFrame
tabela['n_filhos'] = n_filhos
print("DataFrame com a nova coluna 'n_filhos':\n")
print(tabela.head())
print("\n")

# Remove a coluna 'n_filhos' e atualiza o DataFrame
tabela = tabela.drop(['n_filhos'], axis=1)

# Exibe o DataFrame após remover a coluna
print("DataFrame após remover a coluna 'n_filhos':\n")
print(tabela.head())
