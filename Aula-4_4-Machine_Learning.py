import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error # Import mean_squared_error
import tensorflow as tf

# Crie dados fictícios de vendas ao longo do tempo
np.random.seed(42)
meses = np.arange(1, 13)
vendas = np.array([200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480])

# Crie um DataFrame
dados = pd.DataFrame({'Mes': meses, 'Vendas': vendas})

# Visualize os dados
plt.scatter(dados['Mes'], dados['Vendas'])
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Dados de Vendas ao Longo do Tempo')
plt.show()

# Divida os dados em conjunto de treinamento e teste
X = dados[['Mes']]
y = dados['Vendas']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Normalização dos dados de treinamento
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crie e treine o modelo de regressão linear usando TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),  # Camada de entrada
    tf.keras.layers.Dense(units=8, activation='relu'),  # Camada escondida com ativação ReLU
    tf.keras.layers.Dense(units=1)  # Camada de saída
])
model.compile(optimizer='adam', loss='mean_squared_error')

# Treine o modelo por mais épocas
model.fit(X_train_scaled, y_train, epochs=500, verbose=0) # Use scaled data for training

# Faça previsões no conjunto de teste
predictions = model.predict(X_test_scaled) # Predict using scaled data

# Desfaça a normalização para avaliar o desempenho
# Note: y_test does not need inverse scaling for MSE calculation since it's compared with predictions_inverse
predictions_inverse = scaler.inverse_transform(predictions)


# Visualize as previsões em relação aos dados reais
plt.scatter(X_test, y_test, label='Dados Reais') # Use original y_test for plotting
plt.plot(X_test, predictions_inverse, color='red', label='Previsões')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Previsões de Vendas com Regressão Linear (TensorFlow)')
plt.legend()
plt.show()

# Avalie o desempenho do modelo
erro_mse = mean_squared_error(y_test, predictions_inverse) # Calculate MSE with original y_test and inverse-scaled predictions
print(f'Erro Médio Quadrático (MSE): {erro_mse:.2f}')

# Faça uma previsão para o próximo mês
proximo_mes = np.array([[13]])
proximo_mes_scaled = scaler.transform(proximo_mes)
previsao_proximo_mes_scaled = model.predict(proximo_mes_scaled)
previsao_proximo_mes = scaler.inverse_transform(previsao_proximo_mes_scaled)[0, 0]
print(f'Previsão de Vendas para o Próximo Mês: {previsao_proximo_mes:.2f}')