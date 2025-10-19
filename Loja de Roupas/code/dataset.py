import pandas as pd


vendas = pd.read_csv("../data/vendas.csv")
produtos = pd.read_csv("../data/produtos.csv")
clientes = pd.read_csv("../data/clientes.csv")
marketing = pd.read_csv("../data/marketing.csv")
estoque = pd.read_csv("../data/estoque.csv")

clientes.rename(columns={"CPF": "CPF_Cliente"}, inplace=True)

vendas_por_clientes = vendas.merge(clientes,on="CPF_Cliente")



df = vendas.merge(produtos, on="Nome_Produto", how="left")

df

