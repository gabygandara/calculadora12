# Importamos las librerias a utilizar
import streamlit as st
import pandas as pd


# Configuramos la página
st.set_page_config(
    page_title="Calculadora Ahora 12",
    page_icon="📊",
    )


# Columnas superiores
col1, col2, col3 = st.columns(3)

with col1 :
    st.image("imgs/CAME-Transparente.png")

with col2 : 
    st.image("imgs/comercio@4x.png")
    
with col3 :
    st.image("imgs/logo_ahora12.png")

# Titulo
st.title("Calculadora papa")

# Realizamos el input del monto
monto_credito = st.number_input("Ingrese el monto")

# Inputo de la cuota
cuotas = ["Ahora 3","Ahora 6","Ahora 12","Ahora 18","Ahora 24"]
cuota = st.selectbox("Programa",cuotas)    