import pandas as pd
import streamlit as st


vendas = pd.read_csv("../data/vendas.csv")
produtos = pd.read_csv("../data/produtos.csv")
clientes = pd.read_csv("../data/clientes.csv")
marketing = pd.read_csv("../data/marketing.csv")
estoque = pd.read_csv("../data/estoque.csv")

clientes.rename(columns={"CPF":"CPF"}, inplace=True)


vendas['CPF'] = vendas['CPF'].astype(str)
clientes['CPF'] = clientes['CPF'].astype(str)


vendas_por_clientes = vendas.merge(clientes,on="CPF")

df = vendas.merge(produtos, on="Nome_Produto", how="left")
df['Data_Hora'] = pd.to_datetime(df['Data_Hora'])

estoque = estoque.reset_index()
estoque = estoque.rename(columns={'index': 'ID'})




# estoque['ID'] = range(1, len(estoque) + 1)
# estoque['ID'] = estoque['ID'].astype(int)

# estoque['ID'] = estoque['ID'].astype(int)
# estoque['ID'] = estoque['ID'] + 1



