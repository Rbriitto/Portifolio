import streamlit as st
import pandas as pd
from dataset import df, clientes,vendas
from utils import format_number
import datetime


st.set_page_config(layout="wide")

st.title("Loja de Roupas Dashboard ")
aba1, aba2,aba3, aba4= st.tabs(['Dados','Receita', 'Consulta Venda','Estoque'])


st.sidebar.title("Loja de Roupas")

filtros_loja = st.sidebar.multiselect(
    'Loja',df['Local_Venda'].unique()
    
)
filtros_categoria = st.sidebar.multiselect(
    'Categoria', df['Categoria'].unique()
)
filtros_formapgmt = st.sidebar.multiselect(
    'Forma de Pagamento', df['Forma_Pagamento'].unique()
)

if filtros_loja:
    df = df[df['Local_Venda'].isin(filtros_loja)].copy()
    
if filtros_categoria:
    df = df[df['Categoria'].isin(filtros_categoria)].copy()

if filtros_formapgmt:
    df = df[df['Forma_Pagamento'].isin(filtros_formapgmt)].copy()



with aba1:
    st.metric("Receita Total:",format_number(df['Valor_Total'].sum(), 'R$'))
    st.dataframe(df)
    
with aba2:
    st.subheader("Receita por período")
    d = st.date_input("Informe o Período desejado",
                      value=[pd.to_datetime("2025-01-01"), 
                             pd.to_datetime("2025-01-31")])
    
    
    st.metric("Receita Total:",format_number(df['Valor_Total'].sum(), 'R$'))
    
    
    
    
    
with aba3:
    consultacpf = st.text_input("Informe o CPF do Cliente:")
    
    clientefiltro = clientes[clientes['CPF_Cliente'] == consultacpf]
    clientefiltrovendas = vendas[vendas['CPF_Cliente'] == consultacpf]
    
    
    clientefiltro2 = vendas[vendas['CPF_Cliente'] == consultacpf]
    gasto_total = clientefiltro2['Valor_Total'].sum()
    st.metric("Gasto Total do Cliente:", format_number(gasto_total, 'R$'))
    
    consultacpfvendas = consultacpf
    
    # Cliente
    # Vendas 
    
    
    
    st.dataframe(clientefiltro)
    st.dataframe(clientefiltrovendas)
    


          
          
    