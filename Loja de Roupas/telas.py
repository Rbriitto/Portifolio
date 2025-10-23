import streamlit as st
import pandas as pd
from dataset import df,estoque
from utils import format_number, calculo_por_data,consulta_vendas,consulta_estoque
from  datetime import datetime
from visualizandoEstoque import visu


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
    calculo_por_data()   
   
    
with aba3:
    consulta_vendas()
    
with aba4:
    visu()
    #	Produto	Quantidade_Estoque	Data_Entrada	Data_Saida	Fornecedor	Tempo_Medio_Reposicao


          
          
    