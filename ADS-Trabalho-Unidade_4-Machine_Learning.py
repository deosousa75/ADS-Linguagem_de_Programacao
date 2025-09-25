# Passo 1: Importar Bibliotecas e Carregar Dados
# 1.1 - Importar bibliotecas
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# 1.2 - Carregar conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names # Obter os nomes das classes

# Passo 2: Pré-processamento dos Dados
# • Dividir o conjunto de dados em treinamento e teste.
# • Normalizar os dados.

# Passo 2.1 - Dividir o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Passo 2.2 - Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Passo 3: Construir o Modelo
# • Usar TensorFlow para construir um modelo de rede neural simples.

# Construir o modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Passo 4: Treinar o Modelo
# • Treinar o modelo com os dados de treinamento

model.fit(X_train, y_train, epochs=1000, batch_size=32, verbose=0) # verbose=0 para não mostrar o progresso do treinamento

# Passo 5: Avaliar o Modelo
# • Avaliar a precisão do modelo usando os dados de teste.

loss, accuracy = model.evaluate(X_test, y_test, verbose=0) # verbose=0 para não mostrar o progresso da avaliação
print(f'Acurácia do modelo: {accuracy:.4f}')

# Passo 6: Fazer Previsões
# Fazer previsões com o modelo treinado.
# Vamos usar os primeiros 10 exemplos do conjunto de teste para previsão
predictions = model.predict(X_test[:10])

# Mostrar as previsões
print("\nPrevisões para os primeiros 10 exemplos de teste:")
print(predictions)

# Mostrar as classes previstas (índice com maior probabilidade)
predicted_classes = np.argmax(predictions, axis=1)
print("\nClasses previstas para os primeiros 10 exemplos de teste (índices):")
print(predicted_classes)

# Mapear os índices previstos para os nomes das classes
predicted_class_names = [class_names[i] for i in predicted_classes]
print("\nClasses previstas para os primeiros 10 exemplos de teste (nomes):")
print(predicted_class_names)

# Mostrar as classes reais para comparação (nomes)
real_class_names = [class_names[i] for i in y_test[:10]]
print("\nClasses reais para os primeiros 10 exemplos de teste (nomes):")
print(real_class_names)