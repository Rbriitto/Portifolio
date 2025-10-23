import pandas as pd
import streamlit as st
from dataset import vendas


# st.text("Tratamento Possível

# Remover Duplicatas de vendas
# Corrigir datas ou valores inconsistentes
# Calcular ticket médio por venda
# Extrair dia da semana, mês ou sazonalidade

# st.text("Possíveis Insights / Retornos 
# Produtos mais vendidos por período
# Dias/horários de pico de vendas
# Ticket médio por cliente ou por categoria
# Localizações com maior volume de vendas

# Removendo linhas em branco

# st.markdown(f'a tabela possuia [{vendas.shape[0]}] e [{vendas.shape[1]}] colunas')
vendas = vendas.dropna()

# Removendo duplicatas 

vendas = vendas.drop_duplicates()
# st.markdown(f'a tabela possuia [{vendas.shape[0]}] e [{vendas.shape[1]}] colunas')

#Corrigindo data 
#Convertendo data para datetime
vendas['Data_Hora'] = pd.to_datetime(vendas['Data_Hora'])
vendas['Data'] = vendas['Data_Hora'].dt.date
vendas['Hora'] = vendas['Data_Hora'].dt.time
#vendas = vendas.drop(columns=['Data_Hora'])


