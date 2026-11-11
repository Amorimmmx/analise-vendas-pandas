# Trabalho de Python - Análise da Base de Dados de Vendas

import pandas as pd  # Importo o pandas e uso "pd" como apelido.

# Nome do arquivo e texto que indica que o pedido não teve problema.
# Deixei aqui em cima para mudar num lugar só, se precisar.
ARQUIVO = "Base de Dados.xlsx"
SEM_DEVOLUCAO = "Sem devolução"

# Leio o arquivo Excel e guardo a tabela na variável "dados".
dados = pd.read_excel(ARQUIVO)

# Mostro quantas linhas foram carregadas.
total_registros = len(dados)
print("Quantidade de registros:", total_registros)

# Antes de analisar, confiro se tem células vazias ou linhas repetidas.
# isna().sum().sum() soma todas as células vazias da tabela.
print("Células vazias:", int(dados.isna().sum().sum()))
print("Linhas duplicadas:", int(dados.duplicated().sum()))

print("\nPrimeiras linhas da planilha:")
print(dados.head())  # head() mostra cinco linhas por padrão.


# 1. Qual região teve a maior quantidade de vendas?

# "Quantidade de vendas" pode ser lida de três jeitos, então calculei os três
# para ver se a resposta muda: número de registros, unidades vendidas e valor.
registros_por_regiao = dados["Regiao"].value_counts()
unidades_por_regiao = dados.groupby("Regiao")["Quantidade"].sum().sort_values(ascending=False)
valor_por_regiao = dados.groupby("Regiao")["Total"].sum().sort_values(ascending=False)

print("\nRegistros por região:")
print(registros_por_regiao)

print("\nUnidades vendidas por região:")
print(unidades_por_regiao)

print("\nValor total por região:")
print(valor_por_regiao)

# Usei as unidades vendidas como resposta, porque é a coluna "Quantidade".
print("Região com mais vendas:", unidades_por_regiao.idxmax())
print("Unidades vendidas:", int(unidades_por_regiao.max()))


# 2. Qual vendedor teve o maior valor total?

# Agrupo pelo vendedor, somo o "Total" e coloco o maior valor primeiro.
valor_por_vendedor = dados.groupby("Vendedor")["Total"].sum().sort_values(ascending=False)

print("\nValor total por vendedor:")
print(valor_por_vendedor)

print("Vendedor com maior valor total:", valor_por_vendedor.idxmax())
print("Valor total do vendedor:", round(valor_por_vendedor.max(), 2))


# 3. Qual foi o produto mais vendido?

# Somo a coluna "Quantidade" em vez de contar linhas, porque um mesmo
# pedido pode ter várias unidades do produto.
quantidade_por_produto = dados.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

print("\nQuantidade vendida por produto:")
print(quantidade_por_produto)

print("Produto mais vendido:", quantidade_por_produto.idxmax())
print("Unidades vendidas:", int(quantidade_por_produto.max()))


# 4. Qual é a taxa global de devolução?

# Conto os registros em que "Devolucao" é diferente de "Sem devolução".
# A comparação dá True ou False para cada linha e o sum() conta os True.
ocorrencias = (dados["Devolucao"] != SEM_DEVOLUCAO).sum()

# Taxa = ocorrências / total de registros * 100.
# Calculei por registro (cada linha é um pedido).
taxa_devolucao = ocorrencias / total_registros * 100

print("\nOcorrências diferentes de 'Sem devolução':", int(ocorrencias))
print("Total de registros:", total_registros)
print("Taxa global de devolução: {:.2f}%".format(taxa_devolucao))

# Mostro cada tipo de ocorrência para conferir o que entrou na conta.
print("\nTipos de ocorrência:")
print(dados["Devolucao"].value_counts())


# 5. Qual tipo de envio é mais usado?

# Conto quantos registros existem para cada tipo de envio.
envios = dados["Tipo de Envio"].value_counts()

print("\nQuantidade por tipo de envio:")
print(envios)

print("Tipo de envio mais usado:", envios.idxmax())
print("Quantidade de registros:", int(envios.max()))