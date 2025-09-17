import sqlite3

#CREATE (Criação da tabela e inserção de dados de exemplo)
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Contatos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  email TEXT NOT NULL,
  telefone TEXT NOT NULL
)""")
dados_exemplo = [
    ('João', 'joao@email.com', '123456789'),
    ('Maria', 'maria@email.com', '987654321'),
    ('Carlos', 'carlos@email.com', '555555555')
]
cursor.executemany("INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)", dados_exemplo)
conn.commit()

# READ (Letura e exibição dos contatos)
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
for contato in contatos:
    print(f'\nID: {contato[0]}, Nome: {contato[1]}, Email: {contato[2]}, Telefone: {contato[3]}\n')

# UPDATE (Atualização do número de telefone do contato com ID 2)
novo_telefone = '999999999'
contato_id = 2
cursor.execute("UPDATE Contatos SET telefone = ? WHERE id = ?", (novo_telefone, contato_id))
conn.commit()

# DELETE (exclusão do contato com ID 1)
contato_id_para_excluir = 1
cursor.execute("DELETE FROM Contatos WHERE id = ?", (contato_id_para_excluir,))
conn.commit()


# READ (Letura e exibição dos contatos)
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
for contato in contatos:
    print(f'\nID: {contato[0]}, Nome: {contato[1]}, Email: {contato[2]}, Telefone: {contato[3]}\n')


# Fechando a conexão
conn.close()