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
vendas = pd.DataFrame(df_vendas)

print(vendas)


# Fechando a conexão com o banco de dados
conexao.close()


