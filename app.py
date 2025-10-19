import pandas as pd
import streamlit as st
from dataset import df


# Excluindo linhas em branco
df = df.dropna()


print(df['Data_Hora'].dtypes)
df['Data_Hora'] = pd.to_datetime(df['Data_Hora'])

# print(df.dtypes)
#convertendo um valor para data 



# Tratando vendas 



