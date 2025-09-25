from IPython.display import HTML

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Perfil</title>
</head>

<body style="font-family: 'Arial', sans-serif; background-color: #f8f8f8; margin: 0; padding: 0;">

    <header style="text-align: center; background-color: #3498db; color: #fff; padding: 20px;">
        <h1 style="margin: 0;">André Luis da Silva Sousa</h1>
        <p style="margin: 5px 0;">Estudadente de Análise e Desenvolvimento de Sistemas</p>
    </header>

    <section style="margin: 20px; text-align: center;">
        <img src="content/foto.jpg" alt="Foto" style="border-radius: 50%; margin-bottom: 20px;">
        <div id="informacoes-pessoais" style="max-width: 400px; margin: 0 auto;">
            <p>Cidade: Niterói </p>
            <p>País: Brasil</p>
            <p>Interesses: Estágio em Áreas Correlatas a Tecnologia da Informação</p>

        </div>
    </section>
    <section style="margin: 20px; text-align: center;">
        <h2>Habilidades</h2>
        <ul style="list-style: none; padding: 0;">
            <li>Linguagens: Python</li>
            <li>Ferramentas: Git, VS Code, PyCharm</li>
        </ul>
    </section>
    <section style="margin: 20px; text-align: center;">
        <h2>Projeto Recente</h2>
        <p>Trabalhando em pequenos projetos individuis para mostrar meu portfólio.</p>
    </section>
    <footer style="text-align: center; margin-top: 20px;">
        <a href="https://www.linkedin.com/in/andre-l-s-sousa/" target="_blank" style="margin: 0 10px; color: #3498db; text-decoration: none;">LinkedIn</a>
    </footer>
</body>
</html>
"""

# Exibindo a página HTML
HTML(html_code)