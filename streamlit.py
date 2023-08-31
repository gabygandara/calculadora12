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

# Columnas inferiores
col1, col2, col3 = st.columns([0.5,3,0.5])

with col1 :
    st.write("")

with col2 : 
    st.image("imgs/logos_came_recortados.png",use_column_width=True)
    
with col3 :
    st.write("")


st.write("---")
# Realizamos el input del monto
monto_input = st.text_input("Ingrese el monto sin puntos ni comas", value="$")
monto_credito = monto_input.strip()
monto_credito = monto_credito.replace("$", "")
st.write(f"monto : {monto_credito}")

st.write("---")
# Inputo de la cuota
programas = ["Ahora 3","Ahora 6","Ahora 12","Ahora 18","Ahora 24"]
programa_seleccionado = st.selectbox("Seleccione el programa",programas)    

st.write("---")
# Que seleccione 
inscripciones = ["Monotributista", "Responsable Inscripto", "Sociedad"]
tipo_inscripcion = st.selectbox("Seleccione el tipo de inscripción",inscripciones)

st.write("---")

#    # Estilos CSS para el botón
button_style = """
        <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .styled-button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .styled-button:hover {
            background-color: #45a049;
        }
        </style>
    """

    # Insertar estilos CSS en el encabezado de la página
st.markdown(button_style, unsafe_allow_html=True)

    # Diseño centrado con clase "center"
st.write('<div class="center">', unsafe_allow_html=True)
    
    # Botón estilizado con clase "styled-button"
if st.button("Mi Botón", key="my_button"):
    st.write("¡Botón pulsado!")
st.write('</div>', unsafe_allow_html=True)


st.write("---")

st.write("Desarrollado por el departamento de Estadísticas y Bases de datos de CAME")


