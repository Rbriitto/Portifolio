import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# gerando nomes brasileiros
fake = Faker('pt_BR')


# Gerando Clientes

clientes = []
for _ in range(500):
    clientes.append({
        "CPF": fake.cpf(),
        "Nome": fake.name(),
        "Idade": random.randint(18, 65),
        "Sexo": random.choice(["Masculino", "Feminino"]),
        "Localização": fake.city(),
        "Historico_Compras": random.randint(0, 20),
        "Preferencias_Produto": random.choice(["Camisetas", "Calças", "Vestidos", "Acessórios"])
    })
df_clientes = pd.DataFrame(clientes)


# Gerando Produtos

produtos = []
categorias = ["Camisetas", "Calças", "Vestidos", "Acessórios"]
for i in range(1, 21):
    produtos.append({
        "ID_Produto": i,
        "Nome": fake.word().capitalize(),
        "Categoria": random.choice(categorias),
        "Preço_Unitario": round(random.uniform(30, 500), 2),
        "Estoque_Disponivel": random.randint(5, 1000)
    })
df_produtos = pd.DataFrame(produtos)


# Gerando Vendas

vendas = []
for i in range(5000):
    cliente = random.choice(df_clientes["CPF"])  # seleciona um cliente aleatório
    produto = random.choice(df_produtos["ID_Produto"])
    quantidade = random.randint(1, 3)
    df_produto = df_produtos[df_produtos["ID_Produto"] == produto].iloc[0]
    
    vendas.append({
        "ID_Venda": i+1,
        "CPF_Cliente": cliente,            # adicionando cliente à venda
        "Data_Hora": fake.date_time_between(start_date='-6M', end_date='now'),
        "Produto_Comprado": df_produto["Nome"],
        "Quantidade": quantidade,
        "Forma_Pagamento": random.choice(["Cartão", "Dinheiro", "PIX"]),
        "Valor_Total": round(df_produto["Preço_Unitario"] * quantidade, 2),
        "Local_Venda": random.choice(["Loja Física", "Loja Online"])
    })

df_vendas = pd.DataFrame(vendas)


# Gerando Estoque

estoque = []
for produto in produtos:
    estoque.append({
        "Produto": produto["Nome"],
        "Quantidade_Estoque": produto["Estoque_Disponivel"],
        "Data_Entrada": fake.date_this_year(),
        "Data_Saida": fake.date_this_year(),
        "Fornecedor": fake.company(),
        "Tempo_Medio_Reposicao": random.randint(3, 20)  # em dias
    })
df_estoque = pd.DataFrame(estoque)


# Marketing e Engajamento

marketing = []
for i in range(500):
    marketing.append({
        "Campanha": fake.word().capitalize(),
        "Emails_Abertos": random.randint(0, 100),
        "Emails_Clicados": random.randint(0, 50),
        "Cupons_Usados": random.randint(0, 30),
        "Curtidas": random.randint(0, 200),
        "Comentarios": random.randint(0, 50),
        "Cliques_Link_Compra": random.randint(0, 100),
        "Reviews_Produtos": random.randint(0, 50)
    })
df_marketing = pd.DataFrame(marketing)

# Visualizar os dados

df_clientes.to_csv("./data/clientes.csv", index=False, encoding="utf-8-sig")
df_produtos.to_csv("./data/produtos.csv", index=False, encoding="utf-8-sig")
df_vendas.to_csv("./data/vendas.csv", index=False, encoding="utf-8-sig")
df_estoque.to_csv("./data/estoque.csv", index=False, encoding="utf-8-sig")
df_marketing.to_csv("./data/marketing.csv", index=False, encoding="utf-8-sig")

print("Arquivos CSV criados com sucesso!")