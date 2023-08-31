# Importamos las librerias a utilizar
import streamlit as st
import pandas as pd


# Configuramos la página
st.set_page_config(
    page_title="Calculadora Ahora 12",
    page_icon="📊",
    )

# Creamos la tasa de interés
tasas_cft = {"Ahora 3" : 0.1024 ,
         "Ahora 6" : 0.2887 ,
         "Ahora 12" : 0.3297 , 
         "Ahora 18" : 0.4380 ,
         "Ahora 24"  : 0.5221}
aux = False


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

st.write("---")
# Inputo de la cuota
programas = ["Ahora 3","Ahora 6","Ahora 12","Ahora 18","Ahora 24"]
programa_seleccionado = st.selectbox("Seleccione el programa",programas)    

st.write("---")

# Que seleccione 
inscripciones = ["Monotributista", "Responsable Inscripto", "Sociedad"]
tipo_inscripcion = st.selectbox("Seleccione el tipo de inscripción",inscripciones)

st.write("---")


colA, colB = st.columns([1,2])
with colA : 
    if st.button("Calcular"):
                # monto credito
        monto_credito = int(monto_credito)

                # programa seleccionado
        tasas_interes = tasas_cft[programa_seleccionado]

            # Arancel de la tarjeta de credito
        arancel_tarjeta = 0.018

            # Calculamos la tasa del probrama
        base_tasa_programa = monto_credito * tasas_interes

            # Calculamos la base 2
        base_arancel = monto_credito * arancel_tarjeta

            # Iva arancel
        iva_arancel = 0.21 * base_arancel

            # Iva del programa
        iva_programa = 0.105 * base_tasa_programa

            # ingreso bruto
        iibb = 0.025 * base_tasa_programa

            # otro iva
        iva3 = 0.015 * base_tasa_programa

            # total de descuentos
        total_descuentos_1 = base_tasa_programa + iva_arancel + iva_programa + iibb + iva3 + base_arancel

            # neto_percibido
        neto_percibido = monto_credito - total_descuentos_1

            # descuento en %
        total_descuentos_2 = (total_descuentos_1 / monto_credito )

            # monto a cobrar
        monto_a_cobrar = ( 1 / (1-total_descuentos_2) * monto_credito )
        monto_a_cobrar = round(monto_a_cobrar,2)
        monto_final = '{:,.2f}'.format(monto_a_cobrar).replace(',', ' ')
        monto_final = monto_final.replace(".",",")
        monto_final = monto_final.replace(" ",".")

         # reintegro a percibir
        reintegro = iva_arancel + iva_programa + iva3

        # instanciamos aux
        aux = True

with colB:
    if aux == True :
        st.write(f"El precio sugerido es:")
        st.write(f"# $**{monto_final}**")
    else:
         st.write("")    

st.write("Composición del precio sugerido:")
st.write(f"+ Arancel T.Cred (1.8%): **${arancel_tarjeta}**")
st.write("Impuestos:")
st.write(f"+ IVA (21%): **${iva_arancel}**")
st.write(f"+ IVA (10.5%) ley 25.063: **${iva_programa}**")
st.write("Percepciones:")
st.write(f"+ II.BB (2.5%): **${iibb}**")
st.write(f"+ IVA RG2408 (1.5%): **${iva3}**")
st.write(f"+ El precio sugerido es: **${monto_final}**")

if (tipo_inscripcion != "Monotributista"):
    st.write(f"**ATENCIÓN**: Al estar inscripto como {tipo_inscripcion} usted recuperará **${reintegro}** en concepto de IVA")


st.write("---")

st.write("Desarrollado por el departamento de Estadísticas y Bases de datos de CAME")


