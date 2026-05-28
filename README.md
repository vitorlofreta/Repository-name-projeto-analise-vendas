# Projeto de Análise de Vendas

Aluno: Vitor de Araujo Lofreta  
Disciplina: Projeto de Software

# Projeto Análise de Vendas

**Aluno:** Vitor Lofreta
**RA:** 2401019

## Descrição

Este projeto realiza uma análise de dados de vendas utilizando Python, com foco em análise exploratória de dados e Business Intelligence.

O objetivo é organizar, analisar e visualizar dados de vendas por meio de gráficos e dashboards interativos.

---

## Tecnologias utilizadas

* Python
* Pandas
* Matplotlib
* Jupyter Notebook
* Streamlit

---

## Estrutura do projeto

```bash
projeto-analise-vendas/
├── dados/
│   └── vendas.csv
├── notebooks/
│   └── analise_vendas.ipynb
├── app.py
├── README.md
└── MER_Projeto_Analise_de_Vendas.png
```

---

## Funcionalidades

* Leitura de dados CSV
* Tratamento e organização dos dados
* Cálculo de faturamento
* Análise de produtos mais vendidos
* Faturamento por categoria
* Evolução das vendas ao longo do tempo
* Visualização gráfica dos dados
* Dashboard interativo com filtros

---

## Atualização AC2

Nesta etapa foram adicionadas novas análises:

* Faturamento por categoria
* Evolução das vendas ao longo do tempo
* Novos gráficos para visualização

---

## AC3 — Dashboard Interativo

Nesta etapa foi desenvolvido um dashboard utilizando Streamlit para visualização dinâmica dos dados de vendas.

### Funcionalidades do dashboard:

* Filtro por categoria
* Gráfico de produtos mais vendidos
* Gráfico de faturamento
* Visualização temporal das vendas
* Exibição do faturamento total

---

## Modelo Entidade Relacionamento (MER)

O projeto também inclui o Modelo Entidade Relacionamento (MER), representando a estrutura dos dados utilizados na análise.

Entidades modeladas:

* Categoria
* Produto
* Vendas

Relacionamentos:

* Uma categoria pode possuir vários produtos
* Um produto pode estar presente em várias vendas

---

## Como executar

Instale as bibliotecas:

```bash
pip install pandas matplotlib streamlit
```

Depois execute:

```bash
streamlit run app.py
```

O dashboard será aberto no navegador local.

---

## Autor

Vitor Lofreta
RA: 2401019