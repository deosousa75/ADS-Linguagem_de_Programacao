# Tupla de convidados
convidados = ('Alice', 'Bob', 'Carol', "David", 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy')

# Lista de confirmações
confirmados = ['Bob', 'David', 'Frank', 'Judy']

# Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir a lista de convidados
print('\n\033[34mLista de convidados: \033[m')
for pessoa in convidados:
    print(pessoa)
print(f'\033[34mTotal de convidados: {len(convidados)}\033[m')

# Exibir os convidados que ainda não confirmaram
print('\n\033[31mConvidados que ainda não confirmaram: \033[m')
for pessoa in nao_confirmados:
    print(pessoa)
print(f'\033[0;31mTotal de convidados que não confirmaram: {len(nao_confirmados)}\033[m')

# Enviar lembretes aos não confirmados

print('\n\033[33mEnviando lembretes para os convidados que ainda não confirmaram.\n\033[m')