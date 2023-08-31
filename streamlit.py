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
    st.image("imgs/CAME-Transparente.png" )

with col2 : 
    colA, colB = st.columns(2) 
    with colA:
        st.image("imgs/logo_ahora12.png" )
    with colB:
        st.title("Calculadora Ahora 12")
        # Realizamos el input del monto
        monto_credito = st.number_input("Ingrese el monto")
        
        # Inputo de la cuota
        cuotas = ["3","6","12","18","24"]
        cuota = st.selectbox("Cantidad de cuotas",cuotas)



    
with col3 :
    st.image("imgs/comercio@4x.png")
