import matplotlib.pyplot as plt
# Classe para representar um livro
class Livro:
  def __init__(self, titulo, autor, ano_publicacao):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
  def __str__(self):
    return f'\033[32m{self.titulo}\033[0m por \033[33m{self.autor}\033[0m, Publicado em \033[31m{self.ano_publicacao}\033[0m]'

# Criar uma lista de livros
biblioteca = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
  novo_livro = Livro(titulo, autor, ano_publicacao)
  biblioteca.append(novo_livro)
  print(f'{titulo} foi adicionado à biblioteca.')

# Função para listar todos os livros na biblioteca
def listar_livros():
  print()
  for livro in biblioteca:
    print(livro)

# Adicionar alguns livros à biblioteca
adicionar_livro('Dom Quixote','Miguel de Cervantes' , 1605)
adicionar_livro('Orgulho e Preconceito','Jane Austen', 1813)
adicionar_livro('1984','George Orwell', 1949)
adicionar_livro('Cem Anos de Solidão','Gabriel Garcia Marquez', 1967)
adicionar_livro('A Revolução dos Bichos','George Orwell', 1945)
adicionar_livro('Apanhador no Campo de Centeio','J.D. Salinge', 1951)
adicionar_livro('O Alquimista','Paulo Coelho', 1988)
adicionar_livro('O Senhor dos Anéis','J.R.R. Tolkien', 1954)
adicionar_livro('O Pequeno Príncipe','Antoine de Saint-Exupéry', 1943)
adicionar_livro('O Hobbit','J.R.R. Tolkien', 1937)
adicionar_livro('A Culpa é das Estrelas','John Green', 2012)
adicionar_livro('Harry Potter e a Pedra Filosofal','J.K. Rowling', 1997)
adicionar_livro('O Código Da Vinci','Dan Brown', 2003)
adicionar_livro('A Menina que Roubava Livros','Markus Zusak', 2005)
adicionar_livro('O Iluminado','Stephen King', 1977)
adicionar_livro('O Silmarillion','J.R.R. Tolkien', 1977)


# Listar todos os livros na biblioteca
print(f'\n\033[34mLivros Disponíveis na Biblioteca\033[0m')
listar_livros()

# Criar um gráfico de livros por ano
anos = [livro.ano_publicacao for livro in biblioteca]
anos_unicos = list(set(anos)) # Remove duplicatas dos anos
anos_unicos.sort()

# Contagem de livros por ano
contagem_por_ano = [anos.count(ano) for ano in anos_unicos]

# Criar um gráfico de linha
plt.plot(anos_unicos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')

# Adicionar rótulos aos pontos de dados
for i, valor in enumerate(contagem_por_ano):
  plt.text(anos_unicos[i], valor, str(valor), ha='center', va='bottom')
plt.grid(True)

#Salvar o gráfico como imagem (No caso queira salvar)
plt.savefig('livros_por_ano_publicacao.png')  # Salva o gráfico como imagem
print("\nGráfico salvo como 'livros_por_ano_publicacao.png' na pasta atual.\n")

#Exibir o gráfico (Não funcionou no VsCode no Ubuntu)
#plt.show()