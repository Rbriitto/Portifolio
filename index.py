import streamlit as st
import pandas as pd

st.title("Portifólio - Rodrigo Britto")
st.write("[Meu Curriculo](https://curriculo-rodrigobritto.streamlit.app)")
st.write("[GitHub](www.github.com/Rbriitto)")

st.header("Projetos")
st.markdown("---")

st.subheader("Streamlit | Dash ")


col1, col2, col3 = st.columns(3)

st.markdown(""" 
            <style>
            a {
            text-decoration: none !important; /* remove o sublinhado */
            color: #fffff !important /* cor opcional do link */
            font-size:50px !important
            
            }
            a:hover {
            color: #fff; /* muda a cor quando passa o mouse (opcional) */
            }
            </style>
            """, unsafe_allow_html=True)

with col1 :
    st.markdown("""
           
            [Loja de Roupas](Projeto1)


            [Restaurante Delivery](Projeto1)


            [Academia de Ginastica](Projeto1)
            
            
            [Imobiliária](Projeto1)


            [Banco Digital](Projeto1)


            """)
    

with col2:
     st.markdown("""
            [Locadora de Veículos](Projeto1)


            [Supermercado](Projeto1)


            [Clínica Médica](Projeto1)
                 
            
            [Hotel ou Pousada](Projeto1)


            [Empresa de Logística](Projeto1)



            """)
with col2:    
      st.subheader("Python")
      st.markdown("""
            [Analisador de Vendas em CSV](Projeto1)


            [Simulador de Investimentos](Projeto1)


            [Análise de Dados de Funcionários](Projeto1)
            
                  
            [Classificador de Sentimentos Simples](Projeto1)


            [Automatizador de Arquivos](Projeto1)



            """)
     
     
with col3:
      st.markdown("""
            [Loja Virtual (E-commerce](Projeto1)


            [Escola](Projeto1)


            [Plataforma de Streaming](Projeto1)
            
                  
            [Salão de Beleza](Projeto1)


            [Indústria de Alimentos](Projeto1)



            """)    
st.write("---")

with col1:
      st.subheader("Power BI")

      st.markdown("""
            [Startup de Finanças Pessoais](Projeto1)


            [Empresa de Energia Solar](Projeto1)


            [Empresa de Recrutamento](Projeto1)
            
                  
            [Empresa Sustentável (ESG)](Projeto1)


            [Padaria](Projeto1)



            """)    


with col3:
      st.subheader("Java - Spr Boot")

      st.markdown("""
            [Sistema Finanças Pessoais](Projeto1)


            [Sistema de Estoque de Loja](Projeto1)


            [Sistema Escolar](Projeto1)
            
                  
            [Sistema de Aluguel de Veículos](Projeto1)


            [Biblioteca Digital](Projeto1)



            """)    





st.subheader("Dados Utilizados")

st.markdown("""
            [DataSet](Projeto1)

            """)    

st.write("---")











