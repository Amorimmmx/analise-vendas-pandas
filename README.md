# Análise da Base de Dados de Vendas com Python

Projeto de análise de dados em Python e pandas, feito a partir de um desafio proposto no curso do SENAI.

## Sobre o desafio

O professor entregou uma planilha de vendas (`Base de Dados.xlsx`) e pediu que eu usasse Python para responder cinco perguntas de negócio, entregando as respostas junto com o código usado. A avaliação considerava organização, atenção aos detalhes e rigor na criação do código (comentários, importações e afins).

As perguntas foram:

1. Qual região obteve a maior quantidade de vendas?
2. Qual vendedor teve a maior soma de Total (R$)?
3. Qual foi o produto mais vendido?
4. Qual é a taxa de devolução global?
5. Qual é o tipo de envio mais usado?

## Sobre a base

- 1.668 registros de vendas, de 27/12/2014 a 21/09/2015
- 3 lojas (Matriz, On Line e Shopping) e 5 estados
- 20 colunas, como Vendedor, Produto, Quantidade, Preco, Total, Devolucao, Tipo de Envio e Regiao
- Sem células vazias e sem linhas duplicadas

## Resultados

| Pergunta | Resposta |
|---|---|
| 1. Região com mais vendas | **Sudeste** (2.762 unidades) |
| 2. Vendedor com maior soma de Total | **Caio** (R$ 170.454,70) |
| 3. Produto mais vendido | **Calça** (1.761 unidades) |
| 4. Taxa de devolução global | **16,79%** (280 de 1.668 registros) |
| 5. Tipo de envio mais usado | **Loja Física** (798 registros, 47,84%) |

## Como foi feito

1. **Importação:** o pandas lê a planilha Excel e guarda a tabela na variável `dados`.
2. **Conferência:** o código mostra o número de registros, as primeiras linhas e verifica células vazias e linhas duplicadas.
3. **Agrupamento e soma:** com `groupby` e `sum`, calculo o total por região, vendedor e produto.
4. **Contagem:** com `value_counts`, conto registros por região, tipo de devolução e tipo de envio.
5. **Resposta:** com `idxmax`, pego a categoria de maior valor.

Algumas decisões que tomei:

- **Pergunta 1:** "quantidade de vendas" pode ser lida de três formas, então calculei registros, unidades e valor. A resposta é a mesma nas três. Usei as unidades como resposta final.
- **Pergunta 3:** somei a coluna `Quantidade` em vez de contar linhas, porque um pedido pode ter várias unidades do mesmo produto.
- **Pergunta 4:** considerei ocorrência tudo que é diferente de "Sem devolução" (cancelamentos, erro de endereço e extravio). A taxa é por registro.

## Observação sobre os dados

O produto Tênis aparece com preço fixo de R$ 2,30 em todos os registros, enquanto Sapato custa R$ 220,00 e Bota R$ 80,00. Pode ser erro de digitação na base. Isso não muda as respostas acima, mas mudaria uma análise de faturamento por produto.

## Como executar

1. Instale o Python 3.
2. Instale as bibliotecas:

   ```bash
   pip install pandas openpyxl
   ```

3. Deixe `analise_vendas.py` e `Base de Dados.xlsx` na mesma pasta.
4. Rode:

   ```bash
   python analise_vendas.py
   ```

## Estrutura do repositório

```
.
├── analise_vendas.py
├── Base de Dados.xlsx
├── Relatorio_Analise_de_Vendas.pdf
├── requirements.txt
└── README.md
```

## Tecnologias

- Python 3
- pandas
- openpyxl

## Autor

Henrique Amorim
