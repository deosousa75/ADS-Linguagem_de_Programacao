import sqlite3

# Passo 1 - Conectar ao banco de dados SQLite (ou criá-lo, se não existir)
conn = sqlite3.connect('funcionarios.db')

# Passo 2 - Criar a tabela de funcionarios
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL
    )
''')

# Passo 3 - Inserir um novo funcinário na tabela
novo_funcionario = ('João Silva', 'Analista de Sistemas', 5000.00)

cursor.execute('''
    INSERT INTO funcionarios (nome, cargo, salario)
    VALUES (?, ?, ?)
''', novo_funcionario)
conn.commit()

# Passo 4 - Consultar e exibir funcionários
cursor.execute ('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()

print('\n\033[34mFuncionários Cadastrados:\033[0m')
for funcionario in funcionarios:
    print(f'ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Salário: {funcionario[3]:.2f}')

# Passo 5 - Atualizar informações de um funcionário
atualizacao = ('João Silva', 8300.00)
cursor.execute('''UPDATE funcionarios SET salario = ? WHERE nome = ?''', (atualizacao[1], atualizacao[0]))
conn.commit()

# Exibindo os funcionários após a atualização
cursor.execute ('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()
print('\n\033[33mFuncionários Cadastrados:\033[0m')
for funcionario in funcionarios:
    print(f'ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Salário: {funcionario[3]:.2f}')


# Passo 6 - Apagar um funcionário da tabela
id_funcionario_para_apagar = 1
cursor.execute('''DELETE FROM funcionarios WHERE id = ?''', (id_funcionario_para_apagar,))
conn.commit()

# Exibindo os funcionários após a atualização
cursor.execute ('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()
print('\n\033[32mFuncionários Cadastrados:\033[0m')
for funcionario in funcionarios:
    print(f'ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Salário: {funcionario[3]:.2f}')