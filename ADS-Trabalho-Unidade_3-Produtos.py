import sqlite3 # importação da biblioteca SQLite
import pandas as pd # importação da biblioteca Pandas
import matplotlib.pyplot as plt # importação da biblioteca Matplotlib
import seaborn as sns # importação da biblioteca Seaborn

# Passo 1.1 - Conectar ao banco de dados, ou criar, se não existir
conexao = sqlite3.connect('dados_vendas.db')

# Passo 1.2 - Criar um cursor
cursor = conexao.cursor()

# Apagar tabela, se existir (Caso queira reiniciar o processo)
#cursor.execute('''
#  DROP TABLE IF EXISTS vendas1
#  ''')
#conexao.commit()

# Passo 1.3 - Criar uma tabela, se não existir
cursor.execute('''
  CREATE TABLE IF NOT EXISTS vendas1(
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
  )
  ''')

# Passo 1.4 - Inserir alguns dados
cursor.execute('''SELECT COUNT(*) FROM vendas1''')
contador = cursor.fetchone()[0]

if contador == 0:
  cursor.execute('''
        INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
        ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
        ('2023-01-05', 'Produto B', 'Roupas', 350.00),
        ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
        ('2023-03-15', 'Produto D', 'Livros', 200.00),
        ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
        ('2023-04-02', 'Produto F', 'Roupas', 400.00),
        ('2023-05-05', 'Produto G', 'Livros', 150.00),
        ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
        ('2023-07-20', 'Produto I', 'Roupas', 600.00),
        ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
        ('2023-09-30', 'Produto K', 'Livros', 300.00),
        ('2023-10-05', 'Produto L', 'Roupas', 450.00),
        ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
        ('2023-12-20', 'Produto N', 'Livros', 250.00);
    ''')
  conexao.commit()
  print(f"\n\033[32mDados inseridos com sucesso!\n\033[0m")
else:
  print(f"\n\033[31mTabela já contém dados. A inserção foi ignorada.\n\033[0m")

# Passo 2 - Explorar e preparar os dados
df_vendas = pd.read_sql_query('SELECT * FROM vendas1', conexao)
#df_vendas.head()
vendas_lista = df_vendas.to_dict('records') # Convertendo DataFrame para lista de dicionários

# Passo 3 - Analisar os dados
def gerar_grafico_quantidade_vendas_categoria():
  # Criar um gráfico de vendas por categoria
  categoria = [venda['categoria'] for venda in vendas_lista] # Lista de categorias dos produtos
  categorias_unicas = list(set(categoria)) # Remove duplicatas das categorias
  categorias_unicas.sort() # Ordena as categorias alfabeticamente

  # Contagem de vendas por categoria
  contagem_por_categoria = [categoria.count(cat) for cat in categorias_unicas] # Conta quantas vendas há em cada categoria

  # Criar um gráfico de linha de vendas por categoria
  plt.bar(categorias_unicas, contagem_por_categoria, color='darkblue') #
  plt.xlabel('Categoria do Produto') # Rótulo do eixo x
  plt.ylabel('Quantidade de Vendas') # Rótulo do eixo y
  plt.title('Distribuição de Vendas por Categoria de Produto') # Título do gráfico

  # Adicionar rótulos aos pontos de dados
  for i, valor in enumerate(contagem_por_categoria): # Adiciona rótulos aos pontos de dados
    plt.text(categorias_unicas[i], valor, str(valor), ha='center', va='bottom') # Posiciona os rótulos
  plt.grid(True) # Adiciona uma grade ao gráfico
  plt.xticks(rotation=45) # Rotaciona os rótulos do eixo x para melhorar a legibilidade

  #Exibir o gráfico
  plt.tight_layout() # Ajusta o layout do gráfico
  plt.show() # Exibe o gráfico

  # Salvar o gráfico como imagem
  plt.savefig('vendas_por_categoria.png')  # Salva o gráfico como imagem
  print("\nGráfico salvo como 'vendas_por_categoria.png' na pasta atual.\n") # Confirmação de salvamento do gráfico

gerar_grafico_quantidade_vendas_categoria()

# Passo 4 - Visualizar os dados
sns.set(style='whitegrid') # opções: darkgrid, whitegrid, dark, white, ticks

fig, ax = plt.subplots(1, 2, figsize=(15, 5))

sns.barplot(data=df_vendas, x='categoria', y='valor_venda', ax=ax[0])
sns.barplot(data=df_vendas, x='valor_venda', y='produto', ax=ax[1], estimator=sum)
#plt.savefig('grafico_seaborn.png')
#print("\nGráfico salvo como 'grafico_seaborn.png' na pasta atual.\n")
#print('\nFIM DO GRÁFICO SEABORN\n')


# Fechando a conexão com o banco de dados
conexao.close()
