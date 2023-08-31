# Importamos las librerias a utilizar
import streamlit as st
import pandas as pd


# Configuramos la página
st.set_page_config(
    page_title="Calculadora Ahora 12",
    page_icon="📊",
    layout="centered",
    )

# Realizamos el input del monto
monto_credito = st.input()

# Inputo de la cuota
cuotas = ["3","6","12","18","24"]
cuota = st.selectbox("Cantidad de cuotas",cuotas)


# Columnas superiores
col1, col2, col3 = st.columns([1,2,1])

with col1 :
    st.image("imgs/CAME-Transparente.png", use_column_width=True, width=600 , height = 600)

with col2 : 
    colA, colB = st.columns([1,2]) 
    with colA:
        st.image("imgs/logo_ahora12.png", use_column_width=True, width=600 , height = 600)
    with colB:
        st.title("Calculadora Ahora 12")


    

with col3 :
    st.image("imgs/comercio@4x.png", use_column_width=True, width=600, height = 600 )