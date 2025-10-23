import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_csv_aleatorio(nome_arquivo='dados_aleatorios.csv', num_registros=500):
    """
    Gera um arquivo CSV com datas e valores aleatórios.
    
    Args:
        nome_arquivo (str): Nome do arquivo CSV a ser gerado.
        num_registros (int): Número de registros a serem gerados (por padrão, 500).
    """
    
    # 1. Configuração do período para datas aleatórias (2020 a 2024)
    data_inicio = datetime(2020, 1, 1)
    data_fim = datetime(2024, 12, 31)
    
    dados = []
    
    for i in range(num_registros):
        # 2. Gera data aleatória
        dias_aleatorios = random.randint(0, (data_fim - data_inicio).days)
        data_aleatoria = data_inicio + timedelta(days=dias_aleatorios)
        
        # 3. Gera valor aleatório entre 0 e 1000 com 2 casas decimais
        valor_aleatorio = round(random.uniform(0, 1000), 2)
        
        dados.append({
            'data': data_aleatoria.strftime('%Y-%m-%d'),
            'valor': valor_aleatorio
        })
    
    # 4. Cria o DataFrame e salva como CSV
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")
    
    print(f"--- Sucesso! ---")
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
    print(f"Total de registros: {len(dados)}")
    return df

# --- Chamada da função para execução ---
if __name__ == "__main__":
    # Esta linha executa a função com 500 registros
    df_gerado = gerar_csv_aleatorio(nome_arquivo='dados_aleatorios.csv', num_registros=500)
    
    # Exibe uma amostra dos dados gerados
    print("\nDataFrame gerado (apenas as primeiras 5 linhas):")
    print(df_gerado.head())