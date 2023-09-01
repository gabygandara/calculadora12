# Importamos las librerias a utilizar
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

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

monto_input = st.text_input("Ingrese el monto deseado", value="$")
monto_credito = monto_input.strip()
monto_credito = monto_credito.replace("$", "").replace(".","").replace(",,",",").replace(",",".")

if monto_credito == "" or monto_credito == "$" or monto_credito == " " : 
    aux3 = False 
else:
    try:
        monto_credito = float(monto_credito)
        aux3= True
    except ValueError:
        st.text("Coloque un número válido porfavor")
        aux3 = False         

st.write("---")
# Inputo de la cuota
programas = ["Ahora 3","Ahora 6","Ahora 12","Ahora 18","Ahora 24"]
programa_seleccionado = st.selectbox("Seleccione el programa",programas)    

st.write("---")

# Que seleccione 
inscripciones = ["Monotributista", "Responsable Inscripto", "Sociedad"]
tipo_inscripcion = st.selectbox("Seleccione el tipo de inscripción",inscripciones)

st.write("---")

if aux3 == True :

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

    # reintegro a percibir
    reintegro = iva_arancel + iva_programa + iva3


    #descuentos %
    total_descuentos_en_porcentaje = (total_descuentos_1 / monto_credito ) 

    total_descuentos_pesos = monto_a_cobrar * total_descuentos_en_porcentaje

    neto_a_percibir = monto_a_cobrar - total_descuentos_pesos

    # Creamos lista de variables
    lista_variables = [monto_credito, monto_a_cobrar, total_descuentos_pesos, neto_a_percibir, base_tasa_programa, base_arancel, iva_arancel, iva_programa, iibb, iva3, reintegro]

    # iteramos para el formato
    for i in range (len(lista_variables)) :
        lista_variables[i] = '{:,.1f}'.format(lista_variables[i]).replace(',', ' ')
        lista_variables[i] = lista_variables[i].replace(".",",")
        lista_variables[i] = lista_variables[i].replace(" ",".")

    # Nombre del archivo PDF
    pdf_filename = "informe.pdf"

        # Crear un objeto BytesIO para guardar el PDF en memoria
    pdf_buffer = BytesIO()
        # Generar el PDF
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
        
        
        # Agregar título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 770, "Calculadora 12")
        
        # Agregar imagen (ajusta la ruta de la imagen)
    imagen_path = "imgs/CAME-Transparente.png"  # Reemplaza 'tu_imagen.png' con la ruta de tu propia imagen
    c.drawImage(imagen_path, 100, 1, width=200, height=100)

    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Monto actual: ${lista_variables[0]}")
    c.drawString(100, 680, f"Monto a cobrar: {lista_variables[1]}")
    c.drawString(100, 660, f"Total de descuentos: {round(total_descuentos_en_porcentaje,1)*100}%")
    c.drawString(100, 640, f"Total de descuentos en pesos: ${lista_variables[2]}")
    c.drawString(100, 620, f"Neto a percibir: ${lista_variables[3]}")


    c.drawString(100, 580, f"Detalle de descuentos")
    c.drawString(100, 560, f"Tasa del programa {programa_seleccionado} ({tasas_cft[programa_seleccionado]*100}%): ${lista_variables[4]}")
    c.drawString(100, 540, f"Arancel T.Cred (1.8%): ${lista_variables[5]}")
    c.drawString(100, 520, f"IVA (21%): ${lista_variables[6]}")
    c.drawString(100, 500, f"IVA (10.5%) ley 25.063: ${lista_variables[7]}")
    c.drawString(100, 480, f"II.BB (2.5%): ${lista_variables[8]}")
    c.drawString(100, 460, f"IVA RG2408 (1.5%): ${lista_variables[9]}")
    
    if (tipo_inscripcion != "Monotributista"):
        c.drawString(100, 420, f"**ATENCIÓN**: Al estar inscripto como {tipo_inscripcion} usted recuperará **${lista_variables[10]}** en concepto de IVA")

        # Guardar y cerrar el PDF
    c.save()
    pdf_buffer.seek(0)



colA, colB = st.columns([1,2])
with colA : 
    # por las dudas lo guardo :p
    #with st.form("my_form"):
    #    button_clicked = st.form_submit_button("Calcular", help="Haz clic para calcular",use_container_width=True)
    
    #if button_clicked:
        # Cuando se hace clic en el botón, realiza alguna acción
    #    aux = True
    if st.button("Calcular"):
        if aux3 == True :
            aux = True
        else:
            pass  
    if aux == True:
        st.download_button("Descargar PDF", pdf_buffer, file_name="informe.pdf")


with colB:
    
    custom_css = """
        <style>
            .tarjeta {
                text-align: left;
            }
            .subheader {
                font-size: 20px;
                font-weight: bold;
            }
        </style>
        """
        # Agregar el estilo CSS personalizado utilizando st.markdown
        
    if aux == True :
        st.markdown(custom_css, unsafe_allow_html=True)
        monto_final = f"${lista_variables[1]}"
        tarjeta = f'<div class="tarjeta" style="font-size: 45px;font-weight: bold; ">${lista_variables[1]}</div>'
        st.markdown('<div class="subheader">El precio sugerido es:</div>', unsafe_allow_html=True)
        st.markdown(tarjeta, unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)
        #st.write(f"El precio sugerido es:")
        #st.write(f"# $**{monto_final}**")
    else:
         st.write("")    



if aux == True : 
    st.write("---")
    st.write(f"+ ##### Monto actual: ${lista_variables[0]}")
    st.write(f"+ ##### Monto a cobrar: ${lista_variables[1]}")
    st.write(f"+ ##### Total de descuentos: {round(total_descuentos_en_porcentaje,3)*100}%")
    st.write(f"+ ##### Total de descuentos en pesos: ${lista_variables[2]}")
    st.write(f"+ ##### Neto a percibir: ${lista_variables[3]}")




if aux == True : 
    st.write("---")
    st.write("**Detalle de descuentos:**")
    st.write(f"+ Tasa del programa {programa_seleccionado} ({tasas_cft[programa_seleccionado]*100}%): **${lista_variables[4]}**")
    st.write(f"+ Arancel T.Cred (1.8%): **${lista_variables[5]}**")
    st.write(f"+ IVA (21%): **${lista_variables[6]}**")
    st.write(f"+ IVA (10.5%) ley 25.063: **${lista_variables[7]}**")
    st.write(f"+ II.BB (2.5%): **${lista_variables[8]}**")
    st.write(f"+ IVA RG2408 (1.5%): **${lista_variables[9]}**")
    

    if (tipo_inscripcion != "Monotributista"):
        st.write(f"**ATENCIÓN**: Al estar inscripto como {tipo_inscripcion} usted recuperará **${lista_variables[10]}** en concepto de IVA")

st.write("---")

st.markdown("Para mayor información [click aquí](https://www.argentina.gob.ar/ahora-12/comerciantes#:~:text=Ahora%2012%2032%2C97%25%20es%20la%20tasa%20m%C3%A1xima%20de,a%20aplicar%20sobre%20el%20precio%20de%20contado%201%2C664)")


# Agrega CSS personalizado para el marcador en la parte inferior
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 5px;
        text-align: left;
        font-size: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Agrega el marcador
st.markdown('<div class="footer">Desarrollado por el departamento de <a href="https://www.redcame.org.ar/" target="_blank">Estadísticas y Bases de Datos de CAME</a></div>', unsafe_allow_html=True)

