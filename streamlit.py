# Importamos las librerias a utilizar
import streamlit as st
import pandas as pd


# Configuramos la página
st.set_page_config(
    page_title="Calculadora Ahora 12",
    page_icon="📊",
    )

# Titulo centrado con columnas


# Aplicar estilos de formato CSS para agrandar el título
st.markdown("<h1 style='text-align: center; font-size: 60px;'>Calculadora Ahora 12</h1>", unsafe_allow_html=True)

st.write("---")


st.markdown("""
<div style="display: flex; justify-content: center; align-items: center;">
  <img src="imgs/logos_came_recortados.png" alt="Imagen" width="100%" height="100%">
</div>
""", unsafe_allow_html=True)
# Columnas inferiores
col1, col2, col3 = st.columns([0.5,3,1])

with col1 :
    st.write("")

with col2 : 
    st.image("imgs/logos_came_recortados.png",width=600)
    
with col3 :
    st.write("")



# Inputo de la cuota
cuotas = ["Ahora 3","Ahora 6","Ahora 12","Ahora 18","Ahora 24"]
cuota = st.selectbox("Programa",cuotas)    

# Que seleccione 


# Realizamos el input del monto
monto_credito = st.number_input("Ingrese el monto")

st.write("---")

st.write("Desarrollado por el departamento de Estadísticas y Bases de datos de CAME")

