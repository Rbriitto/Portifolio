# Gerando gráficos
from dataset import data
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng
import plotly.express as px



maisouvido = data.groupby('nome_artista')['reproducoes'].sum().reset_index()
# st.bar_chart(maisouvido, x="nome_artista", y="reproducoes", color="#C0C0C0", stack=False)

# 1. Ordena o DataFrame pela coluna "reproducoes" em ordem decrescente (do maior para o menor)
# 2. Seleciona as 10 primeiras linhas (que agora são as 10 maiores)
top_artistas = maisouvido.sort_values(by="reproducoes", ascending=False).head(10)


musicas_mais_ouvidas = data.groupby('nome_musica')['reproducoes'].sum().reset_index()
musicas_mais_ouvidas = musicas_mais_ouvidas.sort_values(by='reproducoes', ascending=False).head(10)

def musicas_mais_ouvidas_fun():
    st.subheader("Top 10 - Musicas Mais Ouvidas")
    st.bar_chart(
        musicas_mais_ouvidas,
        x="nome_musica",
        x_label="Nome da Musica",
        y = "reproducoes",
        y_label="Reproduções",
        color="#57961C",
        horizontal=True
    )



def grafico_artistas():
    st.subheader("Top 10 - Artistas Mais Ouvidos")
    st.bar_chart(
        top_artistas,
        x="nome_artista",
        x_label="Nome do Artista",
        y="reproducoes",
        y_label="Reproduções",
        color="#1C5B96",
        stack=False)

# grafico_artistas()
evolucao_ano = data.groupby('ano_de_lancamento')['reproducoes'].sum().reset_index()
evolucao_ano = evolucao_ano.sort_values(by='ano_de_lancamento')
# data = data[data['ano_de_lancamento'] <= 2023]
# print(data['ano_de_lancamento'].max())

def grafico_evo_ano():
    st.subheader("Evolução por Ano")
    fig = px.line(evolucao_ano, 
                  x='reproducoes', 
                  y='ano_de_lancamento', 
                  markers=True, 
                  title='')
    st.plotly_chart(fig)
    