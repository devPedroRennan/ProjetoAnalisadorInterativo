import streamlit as st
import pandas as pd
import plotly.express as px

def App():
    #variavel que contem o nome das colunas do data frame
    current_df = st.session_state.dfs[0] 
    
    # Variável que contém o nome das colunas do DataFrame
    colunas = current_df.columns

    st.multiselect(
        "Quais colunas deseja analisar", 
        colunas,
        key='choice_columns'
    )

    col1, col2 = st.columns(2, gap = "small")
    
    if col1.button("OK"):
        columns = st.session_state.choice_columns
        if columns:
            st.dataframe(st.session_state.dfs[0][columns])
        else:
            st.warning("Selecione as colunas para visualizar.")
    elif col2.button("Mostrar tudo"):
        st.dataframe(st.session_state.dfs[0])

    st.selectbox(
        "Quais graficos deseja ver?", 
        ("Barras", "Pizza"),
        key = "choice_graphic"
    )

    if st.button("Exibir Gráficos"):
        grafico = st.session_state.choice_graphic
        if grafico == "Barras":
            st.session_station

    
    
