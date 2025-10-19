import streamlit as st
import pandas as pd
from dataset import df, clientes

st.set_page_config(layout="wide")

st.title("Loja de Roupas Dashboard ")
aba1, aba2,aba3 = st.tabs(['Dados','Receita', 'Consulta Venda'])


st.sidebar.title("Loja de Roupas")

with aba1:
    
    st.dataframe(df)
    
with aba3:
    cpf = st.text_input("Informe o CPF do Cliente:")
    st.dataframe(clientes)