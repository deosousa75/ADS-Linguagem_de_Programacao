# PARTE 1 - Matplotlib

import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.plot(dados1, dados2) # pyplot gerencia a figura e o eixo

#Salvar o gráfico como imagem (No caso queira salvar)
plt.savefig('grafico_dados.png')  # Salva o gráfico como imagem
print("\nGráfico salvo como 'grafico_dados.png na pasta atual.\n")

print('\nFIM DO GRÁFICO MATLIBPLOT\n')


# PARTE 2 - Pandas
import pandas as pd
import matplotlib.pyplot as plt # Necessário no VSCode

dados = {
'Produto':['A', 'B', 'C'],
'qtde_vendida':[33, 50, 45]
}
df = pd.DataFrame(dados)

df.plot(x='Produto', y='qtde_vendida', kind='bar')
plt.savefig('grafico_barras.png')

df.plot(x='Produto', y='qtde_vendida', kind='pie')
plt.savefig('grafico_pizza.png')

df.plot(x='Produto', y='qtde_vendida', kind='line')
plt.savefig('grafico_linha.png')

print("\nGráficos salvos como 'grafico_barras.png', 'grafico_pizza.png' e 'grafico_linha.png' na pasta atual.\n")  

print('\nFIM DO GRÁFICO PANDAS\n')


# PARTE 3 - Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='whitegrid') # opções: darkgrid, whitegrid, dark, white, ticks

df_tips = sns.load_dataset('tips')
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
plt.savefig('grafico_seaborn.png')
print("\nGráfico salvo como 'grafico_seaborn.png' na pasta atual.\n")
print('\nFIM DO GRÁFICO SEABORN\n')