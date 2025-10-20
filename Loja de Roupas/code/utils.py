from dataset import df
import pandas as pd
import streamlit as st
import time


#onde as vendas foram realizadas
def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix}{value:.2f} milhões'


#produtos mais vendidos por período

