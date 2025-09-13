import matplotlib.pyplot as plt

# Classe para representar um livro
class Livro: # Define a classe Livro

  def __init__(self, titulo, autor, genero, quantidade): # Construtor da classe Livro
    self.titulo = titulo # Atributo titulo
    self.autor = autor # Atributo autor
    self.genero = genero # Atributo genero
    self.quantidade = quantidade # Atributo quantidade

  def __str__(self): # Método para representar o livro como string
    return f'\033[32m{self.titulo}\033[0m por \033[33m{self.autor}\033[0m, Gênero: \033[31m{self.genero}\033[0m, Quantidade disponível: \033[36m{self.quantidade}\033[0m'

# Criar uma lista de livros
biblioteca = [] # Lista para armazenar os livros

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, genero, quantidade): # Função para adicionar livro
  novo_livro = Livro(titulo, autor, genero, quantidade) # Cria uma nova instância de Livro
  biblioteca.append(novo_livro) # Adiciona o novo livro à lista biblioteca
  print(f'\n\033[32m{titulo}\033[0m foi adicionado à biblioteca.') # Confirmação de adição

# Função para excluir livro da biblioteca
def excluir_livro(titulo): # Função para excluir livro
  for livro in biblioteca: # Percorre a lista de livros
    if livro.titulo.lower() == titulo.lower(): # Verifica se o título corresponde (ignorando maiúsculas/minúsculas)
      biblioteca.remove(livro) # Remove o livro da lista
      print(f'\n\033[31m{titulo} foi removido da biblioteca.\033[m') # Confirmação de remoção
      return # Sai da função após remover o livro
  print('Livro não encontrado.') # Mensagem se o livro não for encontrado

# Função para listar todos os livros na biblioteca
def listar_livros(): # Função para listar livros
  print(f'\n\033[34mLivros Disponíveis na Biblioteca\033[0m')
  for livro in biblioteca: # Percorre a lista de livros
    print(livro)

# Função para buscar livro na biblioteca
def buscar_livro(titulo): # Função para buscar livro
  for livro in biblioteca: # Percorre a lista de livros
    if livro.titulo.lower() == titulo.lower(): # Verifica se o título corresponde (ignorando maiúsculas/minúsculas)
      return livro # Retorna o livro encontrado
  return None # Retorna None se o livro não for encontrado

def gerar_grafico_por_genero():
  # Criar um gráfico de livros por gênero
  generos = [livro.genero for livro in biblioteca] # Lista de gêneros dos livros
  generos_unicos = list(set(generos)) # Remove duplicatas dos generos
  generos_unicos.sort() # Ordena os gêneros alfabeticamente

  # Contagem de livros por gênero
  contagem_por_genero = [generos.count(genero) for genero in generos_unicos] # Conta quantos livros há em cada gênero

  # Criar um gráfico de linha
  plt.bar(generos_unicos, contagem_por_genero, color='darkblue') #
  plt.xlabel('Genero do Livro') # Rótulo do eixo x
  plt.ylabel('Quantidade de Livros') # Rótulo do eixo y
  plt.title('Distribuição de Livros na Biblioteca por Gênero') # Título do gráfico

  # Adicionar rótulos aos pontos de dados
  for i, valor in enumerate(contagem_por_genero): # Adiciona rótulos aos pontos de dados
    plt.text(generos_unicos[i], valor, str(valor), ha='center', va='bottom') # Posiciona os rótulos
  plt.grid(True) # Adiciona uma grade ao gráfico
  plt.xticks(rotation=45) # Rotaciona os rótulos do eixo x para melhorar a legibilidade

  #Exibir o gráfico
  plt.tight_layout() # Ajusta o layout do gráfico
  plt.show() # Exibe o gráfico

  # Salvar o gráfico como imagem
  plt.savefig('livros_por_genero_quantidade.png')  # Salva o gráfico como imagem
  print("\nGráfico salvo como 'livros_por_genero_quantidade.png' na pasta atual.\n") # Confirmação de salvamento do gráfico

# Definição de Menu de Opções
def menu_principal(): # Função para o menu principal
  print('\n\033[35mBem-vindo à Biblioteca Virtual!\033[0m')
  while True: # Loop infinito para o menu
    menu = int(input('\nEscolha a função desejada:\n\n 1 - Cadastrar um Livro\n 2 - Excluir um Título  do Cadastro\n 3 - Exibir Lista de Livros\n 4 - Busca por Livro\n 5 - Exibir Gráfico por Gênero\n 6 - Sair\n\n Digite sua opção:   ')) # Opções do menu
    if menu == 1: # Opção para adicionar livro
      titulo = input('Digite o título do livro: ') # Solicita o título do livro
      autor = input('Digite o autor do livro: ') # Solicita o autor do livro
      genero = input('Digite o gênero do livro: ') # Solicita o gênero do livro
      quantidade = int(input('Digite a quantidade disponível do livro: ')) # Solicita a quantidade disponível do livro
      adicionar_livro(titulo, autor, genero, quantidade) # Chama a função para adicionar o livro

    elif menu == 2: # Opção para excluir livro
      titulo = input('Digite o título do livro que deseja excluir: ') # Solicita o título do livro a ser excluído
      excluir_livro(titulo) # Chama a função para excluir o livro

    elif menu == 3: # Opção para listar livros
      listar_livros() # Chama a função para listar os livros

    elif menu == 4: # Opção para buscar livro
      titulo = input('Digite o título do livro que deseja buscar: ') # Solicita o título do livro a ser buscado
      livro = buscar_livro(titulo) # Chama a função para buscar o livro
      if livro: # Se o livro for encontrado
        print(livro) # Exibe as informações do livro
      else: # Se o livro não for encontrado
        print('Livro não encontrado.') # Mensagem de livro não encontrado

    elif menu == 5: # Opção para gerar gráfico por gênero
      gerar_grafico_por_genero() # Chama a função para gerar o gráfico
      continue

    elif menu == 6: # Opção para sair do programa
      print('\nSaindo do programa...\n') # Mensagem de saída
      break # Sai do loop e termina o programa

    else:
      print('Opção inválida. Tente novamente.') # Mensagem de opção inválida


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

# Iniciar o menu principal
menu_principal() # Chama a função do menu principal

print('\n\033[31mPROGRAMA FINALIZADO\033[0m') # Mensagem de programa finalizado