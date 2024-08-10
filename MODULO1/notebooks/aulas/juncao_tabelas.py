import pandas as pd

# Lê e exibe a tabela de voos
voos = pd.read_csv('./MODULO1/data/aulas/juncao_tabelas/voos.csv', delimiter=';')
print('Voos')
print(voos.head())
print("\n")

# Lê e exibe a tabela de quantidade de voos
qnt_voos = pd.read_csv('C:/Users/carlo/OneDrive/Área de Trabalho/Introducao-Aprendizado-Maquina/MODULO1/data/aulas/juncao_tabelas/quatidade_de_voos.csv', delimiter=';')
print('Quantidade de Voos')
print(qnt_voos.head())
print('\n')

# Unindo as tabelas voos e qnt_voos
print('Merge: Voos + Quantidade de Voos')
voos_completo = pd.merge(voos, qnt_voos, on='month')
print(voos_completo.head())
print('\n')

# Lê e exibe a tabela de produtos1
produtos1 = pd.read_csv('./MODULO1/data/aulas/juncao_tabelas/produtos1.csv', delimiter=';', index_col='id')
print('Produtos 1')
print(produtos1.head())
print('\n')

# Lê e exibe a tabela de produtos2
produtos2 = pd.read_csv('./MODULO1/data/aulas/juncao_tabelas/produtos2.csv', delimiter=';', index_col='id')
print('Produtos 2')
print(produtos2.head())
print('\n')

# Concatenando produtos1 e produtos2 (lado a lado)
produtos = pd.concat([produtos1, produtos2])
print('Produtos (concatenados)')
print(produtos.head(6))
print('\n')

vendas = pd.read_csv('./MODULO1/data/aulas/juncao_tabelas/vendas.csv', delimiter=';')
print('Vendas')
print(vendas.head())
print('\n')

# Mesclando vendas e produtos através do id
vendas = vendas.join(produtos, on = 'produto_id')
print('Vendas de Produtos (junção)')
print(vendas.head()) # Imprime somente o preço dos produtos, mas falta a quantidade total das vendas
print('\n')

# Solução (imprimindo a quantidade total)
print('Vendas de Produtos (total)')
vendas['preco'] = vendas['preco'].str.replace(',', '.').astype(float)
vendas['total'] = vendas['quantidade'] * vendas['preco']
print(vendas.head())
print('\n')