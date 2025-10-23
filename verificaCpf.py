import pandas as pd

# 1. Carregar os dois arquivos CSV em DataFrames
try:
    df1 = pd.read_csv('clientes.csv')
    df2 = pd.read_csv('vendas.csv')
except FileNotFoundError:
    print("Erro: Verifique se os nomes dos arquivos estão corretos.")
    exit()

# Substitua 'CPF' pelo nome real da sua coluna, se for diferente
coluna_cpf = 'CPF_Cliente'

# 2. Realizar a junção (merge) para encontrar CPFs em comum
# 'inner' join garante que apenas as linhas que têm correspondência
# na coluna 'CPF' em AMBOS os DataFrames serão mantidas.
cpfs_em_comum_df = pd.merge(
    df1,
    df2,
    on=coluna_cpf,
    how='inner',
    suffixes=('_arq1', '_arq2') # Adiciona sufixos para diferenciar colunas com o mesmo nome
)

# 3. Selecionar apenas a coluna de CPF para a lista final (removendo duplicatas)
lista_cpfs_comuns = cpfs_em_comum_df[coluna_cpf].unique().tolist()

# 4. Exibir o resultado
print(f"Total de CPFs no Arquivo 1: {len(df1)}")
print(f"Total de CPFs no Arquivo 2: {len(df2)}")
print(f"Total de CPFs encontrados em ambos os arquivos: {len(lista_cpfs_comuns)}")
print("\n--- Lista de CPFs em Comum ---")

# Para imprimir a lista de CPFs:
for cpf in lista_cpfs_comuns:
    print(cpf)

# 5. Opcional: Salvar os CPFs e as informações relacionadas em um novo CSV
cpfs_em_comum_df.to_csv('cpfs_em_comum.csv', index=False)
print("\nArquivo 'cpfs_em_comum.csv' criado com todos os dados dos CPFs que se repetem.")