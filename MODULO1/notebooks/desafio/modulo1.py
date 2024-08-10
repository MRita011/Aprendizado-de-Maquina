# ----------- ENUNCIADO ----------- #

# Muitos pinguins são levados pelas correntezas e acabam nas praias do sul do país. 
# Preocupada com o bem-estar das aves, uma ONG decidiu acolhê-los para posterior reintrodução na natureza.

# Para cada pinguim, foram anotados dados para rastrear sua origem. Informações sobre os pinguins:  
#  - Espécie: atualmente existem 3 espécies “Adelie, Gentoo e Chinstrap”  
#  - Ilha: eles têm vindo de 3 ilhas diferentes “Torgersen, Biscoe e Dream”  

# Foram tiradas as seguintes medidas dos pinguins:  
# - Largura do bico (mm)  
# - Profundidade do bico (mm)  
# - Largura da barbata (mm)  
# - Massa corporal (g)  
# - Sexo: “male” ou “female”  

# A ONG tem quase 350 pinguins, mas alguns dados estão faltando. 
# Seu objetivo é esclarecer a origem de cada pinguim a partir dos dados disponíveis.

# 1. Quais pinguins não têm anotações? 
# 2. Quais ilhas a maioria dos pinguins está vindo? 
# 3. Quais as espécies que a ONG mais possui? 
# 4. Existe alguma relação entre as medidas do pinguim e a sua espécie? 
# 5. Existe alguma relação entre as medidas do pinguim e seu sexo para cada uma das três espécies?   

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo Excel com dados dos pinguins
penguins = pd.read_excel('./MODULO1/data/desafio/Anexo_pinguins-2.xlsx')

# Renomear a coluna para simplificar
penguins.rename(columns={
    'profundidade do bico.1': 'profundidade do bico'
}, inplace=True)

# Excluir a coluna 'data' que foi removida anteriormente
penguins.drop(columns=['profundidade do bico'], inplace=True)

# Exibir as primeiras linhas dos dados
print('\n--------')
print('Pinguins\n--------')
print(penguins.head(7))
print('\n')

# 1. Quais pinguins não têm anotações?
print('--------------------------')
print('Pinguins com Dados Faltantes\n--------------------------')
missing_data = penguins.isnull()
print(missing_data.sum())
print('\n')

# Heatmap para visualizar quais pinguins não têm anotações
missing_data['Pinguim'] = penguins.index

# Transformar o dataframe de dados faltantes para visualização
missing_data = missing_data.set_index('Pinguim')

# Gerar o heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(missing_data, cmap='viridis', cbar_kws={'label': 'Dados Faltantes'})
plt.title('Heatmap de Dados Faltantes nos Pinguins')
plt.xlabel('Atributos')
plt.ylabel('Pinguins')
plt.show()

# 2. Quais ilhas a maioria dos pinguins está vindo?
print('----------------------')
print('Distribuição das Ilhas (que os pinguins veem)\n----------------------')
ilha_counts = penguins['Ilha'].value_counts()
print(ilha_counts)
print('\n')

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(ilha_counts, labels=ilha_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Distribuição dos Pinguins por Ilha')
plt.show()

# 3. Quais as espécies que a ONG mais possui?
print('--------------------------')
print('Distribuição das Espécies que a ONG mais possui\n--------------------------')
especie_counts = penguins['Espece'].value_counts()
print(especie_counts)
print('\n')

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x=especie_counts.index, y=especie_counts.values, palette='viridis')
plt.title('Distribuição das Espécies dos Pinguins na ONG')
plt.xlabel('Espécie')
plt.ylabel('Número de Pinguins')
plt.show()

# 4. Existe alguma relação entre as medidas do pinguim e a sua espécie?
print('----------------------------------')
print('Correlação entre Medidas e Espécie\n----------------------------------')

# Verificar quais colunas numéricas estão presentes
print('Colunas Numéricas Disponíveis:\n', penguins.select_dtypes(include=['float64']).columns)

# Considerando apenas colunas numéricas disponíveis para análise
penguins_numeric = penguins[['largura do bico', 'massa corporal']].copy()
penguins_numeric['Espécie'] = penguins['Espece']

# Criar variáveis dummy para 'Espécie'
penguins_numeric = pd.get_dummies(penguins_numeric, columns=['Espécie'], drop_first=True)

# Calcular a matriz de correlação
correlation_species = penguins_numeric.corr()
print(correlation_species)
print('\n')

# Gerar a matriz de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_species, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Medidas e Espécie')
plt.show()

# 5. Existe alguma relação entre as medidas do pinguim e seu sexo para cada uma das três espécies?
print('---------------------------------------------')
print('Correlação entre Medidas/Sexo por Espécie\n---------------------------------------------')

# Agrupar por espécie e sexo e calcular a média das medidas
grouped = penguins.groupby(['Espece', 'sexo'])[['largura do bico', 'massa corporal']].mean()
print(grouped)
print('\n')

# Gráficos para visualização
# Reshape para visualização
grouped_unstacked = grouped.unstack(level=0)
grouped_unstacked.plot(kind='bar', figsize=(12, 8))
plt.title('Média das Medidas por Sexo e Espécie')
plt.ylabel('Média')
plt.show()