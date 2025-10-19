import pandas as pd


vendas = pd.read_csv("../data/vendas.csv")
produtos = pd.read_csv("../data/produtos.csv")


df = vendas.merge(produtos, on="Nome_Produto", how="left")

df

