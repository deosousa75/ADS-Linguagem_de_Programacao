import pandas as pd

# Criar um dicionário com nomes e idades
dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fabe', 'Gabe'],
    'Idade': [25, 30, 35, 43, 52, 22, 34]
}

# Criar uma série a partir do dicionário
serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])

# Imprimir a série
print('\n\033[34mSérie idades:\033[0m')
print(serie_idades)

# Calcular a media das idades
media_idades = serie_idades.mean()
print(f'\n\033[34mMédia das idades:\033[0m {media_idades:.2f}')