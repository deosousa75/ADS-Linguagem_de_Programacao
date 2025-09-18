import pandas as pd

# Criando um Dataframe com 5 linhas de dados
data = {
    'nome':['Produto A', 'Produto B', 'Produto A', 'Produto D', 'Produto E'],
    'quantidade de itens comprados':[10, 15, 20, 25, 30],
    'tipo de item':['Eletrônico', 'Roupa', 'Eletrônico', 'Roupa', 'Eletrônico'],
    'receita total': [1000, 2000, 3000, 4000, 5000]
}
df = pd.DataFrame(data)

# Exibindo o Dataframe
print(f'\n\033[31mBanco de Dados Inicial:\n\033[0m {df}')

# Excluindo linha duplicada
df.drop_duplicates('nome', keep='last', inplace=True)

# Exibindo o Dataframe
print(f'\n\033[34mBanco de Dados Sem Duplicados:\n\033[0m {df}')

# Incluindo coluna 'preco do item'
df['preco do item'] = df['receita total'] / df['quantidade de itens comprados']

# Exibindo o Dataframe
print(f'\n\033[32mBanco de Dados Com Coluna Preço:\n\033[0m {df}')

# Selecionando preço do item com valor acima ou iguais a 150 reais
itens_acima_de_50 = df[df['preco do item'] >= 150]

# Exibindo o Dataframe 
print(f'\n\033[33mItens com valores maiores ou iguais a 150 Reais:\n\033[0m {itens_acima_de_50}')