import streamlit as st
import pandas as pd
import plotly.express as px

#pegando o arquivo csv do usuario e transformando num data framde
uploaded_files = st.file_uploader("Envie o arquivo csv.", accept_multiple_files=True, type="csv")

#criando uma lista pra armazenar os data frames
dfs = []

#for pra guardar o data frame em variaveis
for uploaded_file in uploaded_files:
    df_temp = pd.read_csv(uploaded_file)
    dfs.append(df_temp)

#variavel que contem o nome das colunas do data frame
colunas = dfs[0].columns

#variavel que guarda o valor das colunas que o usuario quer ver
choices = st.multiselect("Quais colunas deseja analisar", colunas)

#botao pra criar uma visualização grafica do data frame com os filtros
if st.button("OK"):
    st.dataframe(dfs[0][choices])
