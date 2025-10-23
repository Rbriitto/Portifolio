# import pandas as pd
# import streamlit as st
# from  datetime import datetime



# data = pd.read_csv("dados_aleatorios.csv")
# data['data'] = pd.to_datetime(data['data'])
# # print(data.dtypes)

# recebedata = st.date_input(
#     "Informe Data:", 
#                     (data['data'].min(),
#                      data['data'].max()
                               
# ))

# if len(recebedata)==2:
#     dataInicio = pd.to_datetime(recebedata[0])
#     dataFim = pd.to_datetime(recebedata[1])
    
# filtroData = data [
#         (data['data']>= dataInicio) &
#         (data['data']<= dataFim)
        
#     ]
    
# valor_total = filtroData['valor'].sum()

# st.metric(
#     label=f"Valor total de vendas",
#     value =f"R$ {valor_total:.2f}"
# )


# valor = data['valor'].sum()
# st.text(f"Valor por data {valor}")

import pandas as pd
import streamlit as st
from datetime import date

# 1. Carregamento e Preparação dos Dados
# Garante que o arquivo 'dados_aleatorios.csv' está na mesma pasta
try:
    data = pd.read_csv("dados_aleatorios.csv")
    
    # Converte a coluna 'data' para o tipo datetime
    data['data'] = pd.to_datetime(data['data'])
    
except FileNotFoundError:
    st.error("Erro: Arquivo 'dados_aleatorios.csv' não encontrado. Certifique-se de que o arquivo existe.")
    st.stop() # Para a execução do app se o arquivo não for encontrado

# Título da Aplicação
st.title("Análise de Vendas por Período")

# 2. Entrada de Dados (Input do Streamlit)
# Define o intervalo inicial para o date_input como a data mínima e máxima dos dados

data_minima = data['data'].min().date() # Converte para date object para st.date_input
data_maxima = data['data'].max().date()

recebedata = st.date_input(
    "Selecione o Intervalo de Datas:", 
    value=(data_minima, data_maxima),
    min_value=data_minima,
    max_value=data_maxima
)

# 3. Processamento e Filtragem
# Verifica se o usuário selecionou ambas as datas
if len(recebedata) == 2:
    # O Streamlit retorna tuplas de datetime.date, precisamos converter
    data_inicio_selecionada = pd.to_datetime(recebedata[0])
    data_fim_selecionada = pd.to_datetime(recebedata[1])
    
    # O filtro deve ser inclusivo: data >= início E data <= fim
    dados_filtrados = data[
        (data['data'] >= data_inicio_selecionada) & 
        (data['data'] <= data_fim_selecionada)
    ]

    # 4. Cálculo da Soma
    valor_total = dados_filtrados['valor'].sum()
    
    # 5. Exibição do Resultado
    st.metric(
        label=f"Valor Total de Vendas de {recebedata[0]} até {recebedata[1]}", 
        value=f"R$ {valor_total:,.2f}"
    )

    # Opcional: Mostrar os dados filtrados
    # st.subheader("Detalhes dos Registros Filtrados")
    # st.dataframe(dados_filtrados)

else:
    st.info("Por favor, selecione um intervalo de duas datas.")