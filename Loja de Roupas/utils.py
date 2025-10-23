from dataset import df,clientes,estoque
import pandas as pd
import streamlit as st
import time
from vendas import vendas


#onde as vendas foram realizadas
def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix}{value:.2f} milhões'
#produtos mais vendidos por período

def calculo_por_data():
    dados_filtrados = pd.DataFrame()
    data_minima = vendas['Data_Hora'].min().date()
    data_maxima = vendas['Data_Hora'].max().date()
    
  
    
    recebedata = st.date_input(
        'Informe o Período desejado',
        value=(data_minima, data_maxima),
        min_value=data_minima,
        max_value=data_maxima
    )
    
    if len (recebedata) == 2:
        dataInicio = pd.to_datetime(recebedata[0])
        dataFim = pd.to_datetime(recebedata[1])
    
        dados_filtrados = vendas [
            (vendas['Data_Hora'] >= dataInicio) &
            (vendas['Data_Hora'] <= dataFim)
        ]
    
        # somatotal = dados_filtrados["Valor_Total"].sum()
    
        st.metric(f"Valor no período foi",format_number(dados_filtrados['Valor_Total'].sum(), 'R$'))
            
    else:
        st.warning("Selecione as duas datas")      
        
    st.dataframe(dados_filtrados)
    st.markdown(f' A tabela possui :blue[{dados_filtrados.shape[0]}] linhas e :blue[{dados_filtrados.shape[1]}] colunas')

    if 'Valor_Total' in dados_filtrados.columns and len(dados_filtrados) > 0:    
        ticket_medio = dados_filtrados['Valor_Total'].sum() / len(dados_filtrados)
        st.subheader("Ticket Médio por Período")
        st.metric(f"Ticket Médio", format_number((ticket_medio), 'R$'))
    else:
         st.warning("Coluna 'Valor_Total' não encontrada ou sem dados filtrados.")
         
    #st.metric("Receita Total:",format_number(df['Valor_Total'].sum(), 'R$'))

def consulta_vendas():

    consultacpf = st.text_input("Informe o CPF do Cliente:")
    
    clientefiltro = clientes[clientes['CPF'] == consultacpf]
    clientefiltrovendas = vendas[vendas['CPF'] == consultacpf]
    
    
    clientefiltro2 = vendas[vendas['CPF'] == consultacpf]
    gasto_total = clientefiltro2['Valor_Total'].sum()
    
    st.metric("Gasto Total do Cliente:", format_number(gasto_total, 'R$'))      
    
    # consultacpfvendas = consultacpf
    
    relatorio_completo = pd.merge(
            clientefiltro, 
            clientefiltrovendas, 
            on='CPF', 
            how='inner'
        )

    
    st.dataframe(clientefiltro)
    st.dataframe(relatorio_completo)
    
def consulta_estoque():
    st.title("Consulta de Estoque por ID")

    # 1. CAPTURAR O VALOR DO text_input
    # 'consulta_es' será uma string (o que o usuário digita)
    consulta_es = st.text_input("Insira o ID para filtrar:", key="input_consulta_estoque")

    # 2. VERIFICAR SE FOI INSERIDO ALGUM VALOR
    if consulta_es:
        try:
            # Tenta converter o TEXTO (string) em NÚMERO INTEIRO para filtrar a coluna 'ID'
            id_int = int(consulta_es)
            
            # 3. FILTRAR O DATAFRAME
            # Filtra a coluna numérica 'ID' pelo valor numérico 'id_int'
            resultado = estoque[estoque["ID"] == id_int]
            
        except ValueError:
            # Se o usuário digitou letras, a conversão falha
            st.warning("O ID deve ser um número inteiro.")
            return # Sai da função

        # 4. EXIBIR O RESULTADO
        if not resultado.empty:
            st.success(f"Item encontrado para o ID: {id_int}")
            st.dataframe(resultado) 
        else:
            st.warning(f"ID '{id_int}' não encontrado.")
            
# Para filtrar uma COLUNA DE TEXTO (ex: 'Produto'):

def consulta_produto():
    st.title("Consulta de Estoque por Produto")
    
    # Captura o texto (string)
    consulta_produto_text = st.text_input("Digite parte do nome do Produto (Ex: 'Ca')", key="input_consulta_produto")
    
    if consulta_produto_text:
        # Filtra a coluna de texto 'Produto'
        # Usamos '.str.contains' para encontrar qualquer produto que contenha o texto digitado
        # case=False ignora maiúsculas/minúsculas
        resultado = estoque[
            estoque["Produto"].str.contains(consulta_produto_text, case=False)
        ]
        
        if not resultado.empty:
            st.success(f"Produtos que contêm '{consulta_produto_text}':")
            st.dataframe(resultado)
        else:
            st.warning(f"Nenhum produto encontrado com '{consulta_produto_text}'.")
# def consulta_estoque():
#     consulta_es = st.text_input("Insira ID:", key="input_consulta_estoque") 

#     dfFiltro = estoque[estoque['ID'].isin(consulta_es)]
#     st.dataframe(dfFiltro)


    # resultado = pd.DataFrame()
    
    # if consulta_es:
    #     resultado = estoque[estoque['ID'].isin(consulta_es)].copy()      
    #     try:
    #          id_int = int(consulta_es)             
    #          resultado = estoque[estoque["ID"] == id_int]
             
    #     except ValueError:
    #          st.warning("O ID deve ser numérico.")
    #          return
        
    #     if not resultado.empty:
    #          st.dataframe(resultado)
    #     else:
    #          st.warning("ID Não encontrado")
             
             

    
    # consultandoEstoque = estoque[estoque['ID'] == consulta_es]
    # st.dataframe(consultandoEstoque)
  
    
    
    
    
