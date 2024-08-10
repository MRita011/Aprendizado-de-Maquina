import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Carregando os dados
wines = pd.read_excel('./MODULO2/data/aulas/winequality-white.xlsx')
print('------')
print('Wines')
print('------')
print(wines.describe())
print('\n')

# Criando o heatmap
plt.figure(figsize=(12, 8))
heatM = sns.heatmap(wines.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Heatmap da Correlação das Variáveis do Vinho')
plt.show()

# Gerando dados de exemplo
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1) * 0.5

# Visualizando os dados gerados
plt.scatter(X, y)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Dados de Exemplo")
plt.show()

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo de regressão linear
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Realizando previsões nos dados de teste
preds = regressor.predict(X_test)

# Visualizando os resultados
plt.scatter(X_train, y_train, label="Dados de Treino")
plt.plot(X_test, preds, color='red', linewidth=2, label="Previsão")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regressão Linear")
plt.legend()
plt.show()

# Calculando e imprimindo o erro quadrático médio
from sklearn.metrics import mean_squared_error

# Formatando os prints
print('--------------------------------')
print('Erro Quadrático Médio\n--------------------------------')
mse = mean_squared_error(y_test, preds)
print(f'Mean Squared Error: {mse:.4f}')
