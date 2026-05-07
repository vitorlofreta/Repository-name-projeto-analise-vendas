import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# carregar dados
df = pd.read_csv('dados/vendas.csv', sep=';')

# converter data
df["data"] = pd.to_datetime(df["data"], dayfirst=True)

# criar faturamento
df["faturamento"] = df["quantidade"] * df["preco"]

# título
st.title("Dashboard de Vendas")

# filtro
categoria = st.selectbox("Selecione a categoria", df["categoria"].unique())

df_filtrado = df[df["categoria"] == categoria]

# total faturamento
st.write("Faturamento total:", df_filtrado["faturamento"].sum())

# gráfico por produto
fig1, ax1 = plt.subplots()
df_filtrado.groupby("produto")["quantidade"].sum().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# gráfico ao longo do tempo
fig2, ax2 = plt.subplots()
df_filtrado.groupby("data")["faturamento"].sum().plot(kind="line", ax=ax2)
st.pyplot(fig2)