import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('pt_BR')  # para gerar nomes e locais brasileiros

# -----------------------------
# Clientes
# -----------------------------
clientes = []
for _ in range(200):
    # Definindo um número de vendas que este cliente "terá"
    num_vendas_cliente = random.randint(0, 20)
    
    clientes.append({
        "CPF": fake.cpf(),
        "Nome": fake.name(),
        "Idade": random.randint(18, 65),
        "Sexo": random.choice(["Masculino", "Feminino"]),
        "Localização": fake.city(),
        # Usamos o número de vendas gerado para o histórico de compras
        "Historico_Compras": num_vendas_cliente, 
        "Preferencias_Produto": random.choice(["Camisetas", "Calças", "Vestidos", "Acessórios"])
    })
df_clientes = pd.DataFrame(clientes)

# -----------------------------
# Produtos
# -----------------------------
produtos = []
categorias = ["Camisetas", "Calças", "Vestidos", "Acessórios"]
for i in range(1, 540):
    produtos.append({
        "ID_Produto": i,
        "Nome": fake.word().capitalize(),
        "Categoria": random.choice(categorias),
        "Preço_Unitario": round(random.uniform(30, 3000), 2),
        "Estoque_Disponivel": random.randint(5, 5000)
    })
df_produtos = pd.DataFrame(produtos)

# -----------------------------
# Vendas (CORRIGIDO)
# -----------------------------
vendas = []
id_venda_counter = 11  # Contador para o ID da Venda

# Itera sobre cada cliente para gerar as vendas
for index, cliente in df_clientes.iterrows():
    cpf_cliente = cliente["CPF"]
    historico_compras = cliente["Historico_Compras"]
    
    # Gera um número de vendas igual ao Histórico_Compras do cliente
    for _ in range(historico_compras):
        produto = random.choice(df_produtos["ID_Produto"])
        quantidade = random.randint(1, 3)
        df_produto = df_produtos[df_produtos["ID_Produto"] == produto].iloc[0]
        
        vendas.append({
            "ID_Venda": id_venda_counter,
            "CPF": cpf_cliente,  # CPF do cliente atual
            "Data_Hora": fake.date_time_between(start_date='-6M', end_date='now'),
            "Produto_Comprado": df_produto["Nome"],
            "Quantidade": quantidade,
            "Forma_Pagamento": random.choice(["Cartão", "Dinheiro", "PIX"]),
            "Valor_Total": round(df_produto["Preço_Unitario"] * quantidade, 2),
            "Local_Venda": random.choice(["Loja Física", "Loja Online"])
        })
        id_venda_counter += 1 # Incrementa o ID da Venda

df_vendas = pd.DataFrame(vendas)

# -----------------------------
# Verificação (opcional, para testar a correção)
# -----------------------------
# Agrupa as vendas e conta por CPF
contagem_vendas = df_vendas.groupby('CPF').size().reset_index(name='Vendas_Reais')
# Junta com a tabela de clientes para comparar o histórico
df_verificacao = df_clientes.merge(contagem_vendas, on='CPF', how='left').fillna(0)
# Verifica se as vendas reais batem com o histórico
inconsistencias = df_verificacao[df_verificacao['Historico_Compras'] != df_verificacao['Vendas_Reais']]
# print(f"\nTotal de Vendas Geradas: {len(df_vendas)}")
# print(f"Clientes com inconsistências (deve ser 0): {len(inconsistencias)}")
# print("Exemplo de cliente (CPF 647.180.235-80, se existir, terá agora 13 vendas, se o Histórico_Compras for 13):")
# print(df_verificacao[df_verificacao['Historico_Compras'] > 10].head())
# -----------------------------


# -----------------------------
# Estoque
# -----------------------------
estoque = []
for produto in produtos:
    estoque.append({
        "Produto": produto["Nome"],
        "Categoria": random.choice(categorias),
        "Quantidade_Estoque": produto["Estoque_Disponivel"],
        "Data_Entrada": fake.date_this_year(),
        "Data_Saida": fake.date_this_year(),
        "Fornecedor": fake.company(),
        "Tempo_Medio_Reposicao": random.randint(3, 12)  # em dias
    })
df_estoque = pd.DataFrame(estoque)

# -----------------------------
# Marketing e Engajamento
# -----------------------------
marketing = []
for i in range(100):
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

# -----------------------------
# Salvar em CSV
# -----------------------------
df_clientes.to_csv("clientes.csv", index=False, encoding="utf-8-sig")
# df_produtos.to_csv("produtos.csv", index=False, encoding="utf-8-sig")
df_vendas.to_csv("vendas.csv", index=False, encoding="utf-8-sig")
# df_estoque.to_csv("estoque.csv", index=False, encoding="utf-8-sig")
# df_marketing.to_csv("marketing.csv", index=False, encoding="utf-8-sig")

print("Arquivos CSV criados com sucesso! O número de vendas por cliente agora corresponde ao 'Historico_Compras'.")