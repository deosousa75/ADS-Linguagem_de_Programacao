from matplotlib import pyplot as plt

# Dados de exemplo
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas = [120, 90, 150, 80, 200, 150, 300, 100, 180, 500, 110, 773]

#Criar um gráfico (.bar - barras, .plot - linhas, .scatter - pontos)
plt.bar(meses, vendas, color='darkblue')

#Adicionar rótulos aos eixos
plt.xlabel('Mês')
plt.ylabel('Vendas (em unidades)')

#Adicionar um título ao gráfico
plt.title('Vendas Mensais')

#Salvar o gráfico como imagem (No caso queira salvar)
plt.savefig('grafico_vendas.png')  # Salva o gráfico como imagem

#Exibir o gráfico (Não funcionou no VsCode no Ubuntu)
#plt.show()
print("\nGráfico salvo como 'grafico_vendas.png na pasta atual.\n")