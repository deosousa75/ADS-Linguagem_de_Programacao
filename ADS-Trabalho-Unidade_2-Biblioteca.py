import matplotlib.pyplot as plt
# Classe para representar um livro
class Livro:
  def __init__(self, titulo, autor, genero, quantidade):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.quantidade = quantidade
  def __str__(self):
    return f'\033[32m{self.titulo}\033[0m por \033[33m{self.autor}\033[0m, Gênero: \033[31m{self.genero}\033[0m, Quantidade disponível: \033[36m{self.quantidade}\033[0m'

# Criar uma lista de livros
biblioteca = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, genero, quantidade):
  novo_livro = Livro(titulo, autor, genero, quantidade)
  biblioteca.append(novo_livro)
  print(f'{titulo} foi adicionado à biblioteca.')

# Função para excluir livro da biblioteca
def excluir_livro(titulo):
  for livro in biblioteca:
    if livro.titulo.lower() == titulo.lower():
      biblioteca.remove(livro)
      print(f'\n\033[31m{titulo} foi removido da biblioteca.\033[m')
      return
  print('Livro não encontrado.')

# Função para listar todos os livros na biblioteca
def listar_livros():
  print(f'\n\033[34mLivros Disponíveis na Biblioteca\033[0m')
  for livro in biblioteca:
    print(livro)

# Função para buscar livro na biblioteca
def buscar_livro(titulo):
  for livro in biblioteca:
    if livro.titulo.lower() == titulo.lower():
      return livro
  return None

# Definição de Menu de Opções
def menu_principal():
  while True:
    menu = int(input('\nEscolha a função desejada:\n 1 - Cadastrar um Livro\n 2 - Excluir um Título  do Cadastro\n 3 - Exibir Lista de Livros\n 4 - Busca por Livro\n 5 - Exibir Gráfico por Gênero\n 6 - Sair\n'))
    if menu == 1:
      titulo = input('Digite o título do livro: ')
      autor = input('Digite o autor do livro: ')
      genero = input('Digite o gênero do livro: ')
      quantidade = int(input('Digite a quantidade disponível do livro: '))
      adicionar_livro(titulo, autor, genero, quantidade)
    
    elif menu == 2:
      titulo = input('Digite o título do livro que deseja excluir: ')
      excluir_livro(titulo)
      
    elif menu == 3:
      listar_livros()
    
    elif menu == 4:
      titulo = input('Digite o título do livro que deseja buscar: ')
      livro = buscar_livro(titulo)
      if livro:
        print(livro)
      else:
        print('Livro não encontrado.')
    
    elif menu == 5:
      gerar_grafico_por_genero()
      continue
    
    elif menu == 6:
      print('Saindo do programa...')
      break
    
    else:
      print('Opção inválida. Tente novamente.')

def gerar_grafico_por_genero():
  # Criar um gráfico de livros por gênero
  generos = [livro.genero for livro in biblioteca]
  generos_unicos = list(set(generos)) # Remove duplicatas dos generos
  generos_unicos.sort()

  # Contagem de livros por gênero
  contagem_por_genero = [generos.count(genero) for genero in generos_unicos]

  # Criar um gráfico de linha
  plt.plot(generos_unicos, contagem_por_genero, marker='o', linestyle='-')
  plt.xlabel('Genero do Livro')
  plt.ylabel('Quantidade de Livros')
  plt.title('Distribuição de Livros na Biblioteca por Gênero')

  # Adicionar rótulos aos pontos de dados
  for i, valor in enumerate(contagem_por_genero):
    plt.text(generos_unicos[i], valor, str(valor), ha='center', va='bottom')
  plt.grid(True)

  #Salvar o gráfico como imagem
  plt.savefig('livros_por_genero_quantidade.png')  # Salva o gráfico como imagem
  print("\nGráfico salvo como 'livros_por_genero_quantidade.png' na pasta atual.\n")

  #Exibir o gráfico   
  plt.show()
  
# Adicionando alguns livros à biblioteca para povoar o catálogo
adicionar_livro('Dom Quixote','Miguel de Cervantes', 'Romance', 10)
adicionar_livro('Orgulho e Preconceito','Jane Austen', 'Romance', 5)
adicionar_livro('1984','George Orwell', 'Ficção Científica', 3)
adicionar_livro('Cem Anos de Solidão','Gabriel Garcia Marquez', 'Romance', 8)
adicionar_livro('A Revolução dos Bichos','George Orwell', 'Sátira', 3)
adicionar_livro('Apanhador no Campo de Centeio','J.D. Salinge', 'Romance', 9)
adicionar_livro('O Alquimista','Paulo Coelho', 'Filosofia', 2)
adicionar_livro('O Senhor dos Anéis','J.R.R. Tolkien', 'Aventura', 7)
adicionar_livro('O Pequeno Príncipe','Antoine de Saint-Exupéry', 'Fábula', 4)
adicionar_livro('O Hobbit','J.R.R. Tolkien', 'Aventura', 4)
adicionar_livro('A Culpa é das Estrelas','John Green', 'Drama', 8)
adicionar_livro('Harry Potter e a Pedra Filosofal','J.K. Rowling', 'Fantasia', 6)
adicionar_livro('O Código Da Vinci','Dan Brown', 'Romance', 4)
adicionar_livro('A Menina que Roubava Livros','Markus Zusak', 'Drama', 5)
adicionar_livro('O Iluminado','Stephen King', 'Suspense', 3)
adicionar_livro('O Silmarillion','J.R.R. Tolkien', 'Fantasia', 5)

''' Mais alguns livros para adicionar manualmente:
O Nome do Vento, Patrick Rothfuss, Fantasia;
O Morro dos Ventos Uivantes, Emilu Bronte, Romance;
A Metamorfose, Franz Kafka, Ficção Científica;
O Grande Gatsby, F. Scott Fitzgerald, Romance;
Neuromancer, William Gibson, Ficção Científica;
'''

menu_principal()

print('\n\033[31mPROGRAMA FINALIZADO\033[0m')