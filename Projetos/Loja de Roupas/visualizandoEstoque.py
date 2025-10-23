import streamlit as st
from dataset import estoque
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Busca ID", layout="wide")
df = pd.DataFrame(estoque)

def visu():


# Interface
    st.title('🔍 Busca por ID')

    # Controles
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        id_input = st.text_input('Digite o ID para buscar:', placeholder='Ex: 1005')

    with col2:
        mostrar_todos = st.checkbox('Mostrar todos os dados', value=True)

    with col3:
        if st.button('Limpar Busca'):
            id_input = ''
            st.rerun()

    # Processamento da busca
    if id_input:
        try:
            id_alvo = int(id_input)
            
            # Buscar o registro
            registro = df[df['ID'] == id_alvo]
            
            if not registro.empty:
                st.success(f'✅ ID {id_alvo} encontrado!')
                
                # Mostrar detalhes do registro
                with st.container():
                    st.markdown("### 📋 Detalhes do Registro")
                    for col in registro.columns:
                        st.write(f"**{col}:** {registro[col].iloc[0]}")
                
                # Mostrar dataframe com destaque
                if mostrar_todos:
                    st.markdown("### 📊 Visualização com Destaque")
                    
                    def aplicar_destaque(row):
                        if row['ID'] == id_alvo:
                            return ['background-color: #800000'] * len(row)
                        return [''] * len(row)
                    
                    st.dataframe(
                        df.style.apply(aplicar_destaque, axis=1),
                        use_container_width=True
                    )
            else:
                st.error(f'❌ ID {id_alvo} não encontrado!')
                
        except ValueError:
            st.error('⚠️ Por favor, digite um número válido para o ID')

    else:
        if mostrar_todos:
            st.markdown("### 📊 Base de Dados Completa")
            st.dataframe(df, use_container_width=True)