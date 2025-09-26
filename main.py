import streamlit as st
import pandas as pd
import plotly.express as px
import app

if 'dfs' not in st.session_state:
    st.session_state.dfs = []

st.title("Analisador de Dados Interativo")

st.session_state['dfs'] = []

#pegando o arquivo csv do usuario e transformando num data framde
uploaded_files = st.file_uploader("Envie o arquivo csv.", accept_multiple_files=True, type="csv")

#criando uma lista pra armazenar os data frames
dfs = []

#for pra guardar o data frame em variaveis
for uploaded_file in uploaded_files:
    df_temp = pd.read_csv(uploaded_file)
    dfs.append(df_temp)

#verifica se o data frame possui algo pra o armazenar
if dfs:
    st.session_state['dfs'] = dfs

#verifica pra executar o app
if st.session_state.dfs:
    app.App()
    #botao pra criar uma visualização grafica do data frame com os filtros
    
