# Importe as bibliotecas necessárias
import numpy as np

# Dados dos participantes
participantes = [
    {
        'nome': 'Alice',
        'localizacao': 'EUA',
        'afiliacao': 'Universidade Alfa',
        'interesses': ['Física', 'Astronomia']
    },
    {
        'nome': 'Bob',
        'localizacao': 'Brasil',
        'afiliacao': 'Instituto Bravo',
        'interesses': ['Biologia', 'Astronomia']
    },
    {
        'nome': 'Charlie',
        'localizacao': 'Índia',
        'afiliacao': 'Instituto Casa',
        'interesses': ['Química', 'Engenharia']
    },
    {
        'nome': 'Diófenes',
        'localizacao': 'Grécia',
        'afiliacao': 'Instituto Delta',
        'interesses': ['Arquitetura', 'Matemática']
    },
    {
        'nome': 'Esmeralda',
        'localizacao': 'França',
        'afiliacao': 'Instituto Bravo',
        'interesses': ['Geografia', 'Matemática', 'Física']
    }
    # Adicione mais participantes conforme necessário
]

# Usando sets para identificar diferentes regiões dos participantes
regioes = set(participante['localizacao'] for participante in participantes) # Conjunto de regiões únicas

# Usando um dicionário para categorizar afiliações
afiliacoes = {} # Dicionário para armazenar afiliações e seus membros
for participante in participantes: # Itera sobre cada participante
    afiliacao = participante['afiliacao'] # Obtém a afiliação do participante
    if afiliacao not in afiliacoes: # Se a afiliação ainda não estiver no dicionário
        afiliacoes[afiliacao] = [] # Inicializa uma lista para essa afiliação
    afiliacoes[afiliacao].append(participante['nome']) # Adiciona o nome do participante à lista da afiliação

# Usando NumPy para analisar áreas de interesse
areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante['interesses']]) # Array de todas as áreas de interesse
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True) # Identifica áreas únicas e suas contagens
area_mais_popular = interesses_unicos[np.argmax(contagem)] # Área de interesse mais popular


# Resultados
print('\nRegiões dos participantes:', regioes) # Imprime as regiões únicas dos participantes
print('\nAfiliações dos participantes:') # Imprime as afiliações e seus membros

for afiliacao, nomes in afiliacoes.items(): # Itera sobre cada afiliação e seus membros
    print(f'{afiliacao}: {', '.join(nomes)}') # Imprime a afiliação e os nomes dos membros

print('\nÁrea de interesse mais popular:', area_mais_popular) # Imprime a área de interesse mais popular