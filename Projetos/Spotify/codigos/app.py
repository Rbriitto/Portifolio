import pandas as pd
import streamlit as st
from dataset import data
from graph import grafico_artistas, grafico_evo_ano, musicas_mais_ouvidas_fun

st.set_page_config(layout="wide")
aba1, aba2 = st.tabs(['Dataset', 'Graficos'])


with aba1:
    st.title("Análise Spotify 2023")
    st.dataframe(data)
   
    
with aba2:
    col1, col2 = st.columns(2)
    with col1:
        grafico_artistas()
        musicas_mais_ouvidas_fun()
        
    with col2:
        grafico_evo_ano()



