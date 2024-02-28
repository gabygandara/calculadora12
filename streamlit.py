# Importamos las librerias a utilizar
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import datetime
import pytz
import time
import pandas as pd
from github import Github
import io
import github
import requests
import geocoder
import webbrowser

# Configuramos la página
st.set_page_config(
    page_title="Calculadora Cuota Simple",
    page_icon="imgs/CAME-Transparente.ico.ico",
    )
# Configura el repositorio de GitHub y el archivo CSV
github_token = st.secrets["TOKEN"]
repo_name = st.secrets["REPO"]

# Inicializar st.session_state
if 'aux2' not in st.session_state:
    st.session_state.aux2 = False

# Inicializar st.session_state
if 'submit_button' not in st.session_state:
    st.session_state.submit_button = False

# Inicializar st.session_state
if 'monto_credito' not in st.session_state:
    st.session_state.monto_credito = False

# Inicializar st.session_state
if 'programa_seleccionado' not in st.session_state:
    st.session_state.programa_seleccionado = False

# Inicializar st.session_state
if 'carga_inicial' not in st.session_state:
    st.session_state.carga_inicial = False
        
        
# Inicializar st.session_state
if 'tipo_inscripcion' not in st.session_state:
    st.session_state.tipo_inscripcion = False
# Inicializar st.session_state
if 'provincia_seleccionada' not in st.session_state:
    st.session_state.provincia_seleccionada = False

# Creamos la función para agregar datos    
def calculo(fecha_actual, hora_actual, lista_variables1, lista_variables2, programa_seleccionado, tipo_inscripcion, provincia_seleccionada):
    # Configura el repositorio de GitHub y el archivo CSV
    file_path = st.secrets["ARCHIVO_CALCULADORA"]
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    contents = repo.get_contents(file_path)
    # Create a file-like object from the decoded content
    content_bytes = contents.decoded_content
    content_file = io.BytesIO(content_bytes)
    # Read the CSV from the file-like object
    df = pd.read_csv(content_file)

    # Espera de 1 segundo
    time.sleep(0.5) 

    # Create a DataFrame with the new data
    new_data = pd.DataFrame({
        'Fecha': [fecha_actual],
        'Hora': [hora_actual],
        'Monto': [lista_variables1],
        'Precio Sugerido': [lista_variables2],
        'Programa': [programa_seleccionado],
        'Tipo de inscripcion': [tipo_inscripcion],
        'Provincia': [provincia_seleccionada]
    })
    # Append the new DataFrame to the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)
    # Save the updated DataFrame back to the file-like object
    content_file.seek(0)  # Reset the file position to the beginning
    df.to_csv(content_file, index=False)

    # Espera de 1 segundo
    time.sleep(0.5) 

    # Update the file in the repository with the modified content
    repo.update_file(contents.path, "Actualizado el archivo CSV", content_file.getvalue(), contents.sha)

# Creamos la función para agregar datos    
def consulta(fecha_actual, hora_actual, nombre_ingresado, apellido_ingresado, email_ingresado, repetir_email_ingresado ,asunto_ingresado, consulta_ingresada):
    file_path = st.secrets["ARCHIVO_CONSULTAS"]
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    contents = repo.get_contents(file_path)
    # Create a file-like object from the decoded content
    content_bytes = contents.decoded_content
    content_file = io.BytesIO(content_bytes)
    # Read the CSV from the file-like object
    df = pd.read_csv(content_file)

    # Espera de 1 segundo
    time.sleep(0.5) 

    # Create a DataFrame with the new data
    new_data = pd.DataFrame({
        'Fecha': [fecha_actual],
        'Hora': [hora_actual],
        'Nombre': [nombre_ingresado],
        'Apellido': [apellido_ingresado],
        'Mail': [email_ingresado],
        'Mail 2': [repetir_email_ingresado],
        'Asunto': [asunto_ingresado],
        'Consulta': [consulta_ingresada],
    })
    # Append the new DataFrame to the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)
    # Save the updated DataFrame back to the file-like object
    content_file.seek(0)  # Reset the file position to the beginning
    df.to_csv(content_file, index=False)

    # Espera de 1 segundo
    time.sleep(0.5) 

    # Update the file in the repository with the modified content
    repo.update_file(contents.path, "Actualizado el archivo CSV", content_file.getvalue(), contents.sha)  

# Creamos la función para agregar datos    
def calificacion(fecha_actual, hora_actual, evaluation):
    # Configura el repositorio de GitHub y el archivo CSV
    file_path = st.secrets["ARCHIVO_CALIFICACION"]  
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    contents = repo.get_contents(file_path)
    # Create a file-like object from the decoded content
    content_bytes = contents.decoded_content
    content_file = io.BytesIO(content_bytes)
    # Read the CSV from the file-like object
    df = pd.read_csv(content_file)

    # Espera de 1 segundo
    time.sleep(0.5) 

    # Create a DataFrame with the new data
    new_data = pd.DataFrame({
        'Fecha': [fecha_actual],
        'Hora': [hora_actual],
        'Evaluación': [evaluation],
    })
    # Append the new DataFrame to the existing DataFrame
    df = pd.concat([df, new_data], ignore_index=True)
    # Save the updated DataFrame back to the file-like object
    content_file.seek(0)  # Reset the file position to the beginning
    df.to_csv(content_file, index=False)

    # Espera de 1 segundo
    time.sleep(0.5) 

    # Update the file in the repository with the modified content
    repo.update_file(contents.path, "Actualizado el archivo CSV", content_file.getvalue(), contents.sha)        

# Aplicar estilos de formato CSS para agrandar el título
st.markdown("<h1 style='text-align: center; font-size: 54px; font-family: Verdana, sans-serif;'>Calculadora<br>Cuota Simple</h1>", unsafe_allow_html=True)

st.write("---")

# Columnas inferiores
col1, col2, col3 = st.columns([0.5,3,0.5])

with col1 :
    st.write("")

with col2 : 
    st.image("imgs/logos_came_con_fondo y recortados.png",use_column_width=True)
    
with col3 :
    st.write("")


# INPUT CALCULADORA
with st.form(key='calculator_form'):
    # Ingresa el valor
    monto_input = st.text_input("Precio contado", value="$")
    # Se formatea el valor ingresado
    monto_credito = monto_input.strip()
    monto_credito = monto_credito.replace("$", "").replace(".","").replace(",,",",").replace(",",".")  

    columna_programa, columna_inscripcion, columna_provincia = st.columns(3)
    with columna_programa:
        # Seleccionar el programa
        programas = ["-", "3 Cuotas", "6 Cuotas"]
        programa_seleccionado = st.selectbox("Seleccione el programa",programas)  

    with columna_inscripcion:
        # Seleccionar tipo de inscripción
        inscripciones = ["-", "Monotributista", "Responsable Inscripto", "Sociedad"]
        tipo_inscripcion = st.selectbox("Seleccione el tipo de inscripción",inscripciones)

    with columna_provincia:
        # listado de provincias
        provincias = [
            "-",
            "Buenos Aires",
            "CABA",
            "Catamarca",
            "Chaco",
            "Chubut",
            "Córdoba",
            "Corrientes",
            "Entre Ríos",
            "Formosa",
            "Jujuy",
            "La Pampa",
            "La Rioja",
            "Mendoza",
            "Misiones",
            "Neuquén",
            "Río Negro",
            "Salta",
            "San Juan",
            "San Luis",
            "Santa Cruz",
            "Santa Fe",
            "Santiago del Estero",
            "Tierra del Fuego",
            "Tucumán"
        ]

        # Seleccionar provincia
        provincia_seleccionada = st.selectbox("Seleccione su provincia",provincias)  

    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.write("")
    with col2:
        # Botón de calcular
        submit_button = st.form_submit_button(label='**Calcular**',use_container_width=True)
    with col2:
        st.write("")
    

    # Inicia el cálculo
    if submit_button:
        try:
            # Auxiliar1 para controlar el mensaje de error
            aux1= False
            monto_credito = float(monto_credito)  
            if  (programa_seleccionado == "-") or (tipo_inscripcion == "-") or (provincia_seleccionada == "-"):
                aux1 = True 
                raise ValueError("")  

            # INSTANCIAMOS TODAS LAS VARIABLES  
            st.session_state.aux2 = True
            st.session_state.monto_credito = monto_credito
            st.session_state.programa_seleccionado = programa_seleccionado
            st.session_state.tipo_inscripcion = tipo_inscripcion
            st.session_state.provincia_seleccionada = provincia_seleccionada
            st.session_state.submit_button = True
            st.session_state.carga_inicial = False

        except ValueError: 
            aux2 = False   
            # Mensaje de error 1
            if (aux1 == False):
                st.error("Ingrese un monto válido porfavor.")
            # Mensaje de error 2
            else:
                st.error("Complete los campos necesarios porfavor.")

# CHECKEO DE AUXILIAR PARA AVANZAR CÁLCULO 
# Inicia el cálculo
if (st.session_state.submit_button == True):       
    if (st.session_state.aux2 == True): 
        with st.spinner("Cargando . . ."): 

            tasas_cft = {
                        "3 Cuotas" : 0.1076,
                        "6 Cuotas" : 0.1976 }
            # PARA AVANZAR EL CÁLCULO
            if ("Responsable" in st.session_state.tipo_inscripcion) or (st.session_state.tipo_inscripcion == "Sociedad"):
                st.session_state.tipo_inscripcion = "Responsable" 
                # COEFICIENTES PARA SOCIEDAD - RI
                coeficientes = {
                        "3 Cuotas" : 1.1622 ,
                        "6 Cuotas" : 1.3444 }  
                    
            elif (st.session_state.tipo_inscripcion == "Monotributista"):
                # COEFICIENTES PARA MONOTRIBUTISTA
                coeficientes = {
                        "3 Cuotas" : 1.1428 ,
                        "6 Cuotas" : 1.2922 }      
                      
            
            # OBTENEMOS LA TASA DEL PROGRAMA
            tasa_programa = tasas_cft[st.session_state.programa_seleccionado]

            # Obtenemos el coeficiente
            coeficiente = coeficientes[st.session_state.programa_seleccionado]
                
            # ---
            # LIQUIDACIÓN DE PAGO
            # ---

            # PRIMER CALCULO
            precio_sugerido = st.session_state.monto_credito * coeficiente

            # SEGUNDO CALCULO   
            arancel_1_8 = 0.018 * precio_sugerido

            # TERCER CALCULO
            costo_financiero = tasa_programa * precio_sugerido

            # CUARTO CALCULO
            iva_arancel = 0.21 * arancel_1_8

            # QUINTO CALCULO
            iva_costo_financiero = costo_financiero * 0.105

            # CALCULAMOS EL SUBTOTAL
            subtotal = precio_sugerido - (arancel_1_8 + costo_financiero + iva_arancel+ iva_costo_financiero )

            # SEXTO CALCULO
            iva_rg = subtotal * 0.03

            # CALCULAMOS EL TOTAL COBRADO EN LA LIQUIDACIÓN
            total_cobrado_liquidacion = subtotal - iva_rg

            # ---
            # CALCULO DE IMPUESTOS 
            # ---

            # Definimos la tasa municipal
            porcentaje_municipal = 0.01

            

            if "Monotributista" in st.session_state.tipo_inscripcion:
                # INGRESOS BRUTOS MONOTRIBUTISTA
                iibb = precio_sugerido * 0.035
                # PRIMER CALCULO
                venta_neta_iva = 0

                # SEGUNDO CALCULO
                iva_debito = 0

                # TERCER CALCULO
                iva_credito = 0

                # CUARTO CALCULO
                posicion_iva = 0

                # QUINTO CALCULO
                saldo_cobrado = total_cobrado_liquidacion - posicion_iva

            elif "Responsable" in st.session_state.tipo_inscripcion:
                # PRIMER CALCULO
                venta_neta_iva = precio_sugerido / (1+ 0.21)
                
                # INGRESOS BRUTOS RESPONSABLE
                iibb = venta_neta_iva * 0.035
                
                # SEGUNDO CALCULO
                iva_debito = venta_neta_iva * 0.21

                # TERCER CALCULO
                iva_credito = iva_arancel + iva_costo_financiero + iva_rg

                # CUARTO CALCULO
                posicion_iva = iva_debito - iva_credito

                # QUINTO CALCULO
                saldo_cobrado = total_cobrado_liquidacion - posicion_iva

            # SEXTO
            if "Monotributista" in st.session_state.tipo_inscripcion:
                tasa_municipal = precio_sugerido * porcentaje_municipal

            elif "Responsable" in st.session_state.tipo_inscripcion:
                tasa_municipal = venta_neta_iva * porcentaje_municipal



            # OCTAVO CALCULO
            utilidad_antes_de_costos = saldo_cobrado - tasa_municipal - iibb

            # DEFINIMOS ALGUNAS VARIABLES
            total_descuento_pesos = precio_sugerido - st.session_state.monto_credito 
            tasas_a_STR = str(tasas_cft[st.session_state.programa_seleccionado]*100).replace(".",",")
            alicuota_a_STR = "3,5"
                
            # Creamos lista de variables
            lista_variables = [st.session_state.monto_credito , precio_sugerido, arancel_1_8, costo_financiero, iva_arancel, iva_costo_financiero, subtotal, iva_rg, total_cobrado_liquidacion, venta_neta_iva, iva_debito, iva_credito, posicion_iva, saldo_cobrado, tasa_municipal, iibb, utilidad_antes_de_costos, total_descuento_pesos]
                
            # iteramos para el formato
            for i in range (len(lista_variables)) :
                lista_variables[i] = '{:,.2f}'.format(lista_variables[i]).replace(',', ' ')
                lista_variables[i] = lista_variables[i].replace(".",",")
                lista_variables[i] = lista_variables[i].replace(" ",".")


            # PARA ARMAR EL PDF                
            pdf_filename = "Resumen precio sugerido.pdf"

                # Crear un objeto BytesIO para guardar el PDF en memoria
            pdf_buffer = BytesIO()
                # Generar el PDF
            c = canvas.Canvas(pdf_buffer, pagesize=letter)

            # Establecer la zona horaria a Buenos Aires
            zona_horaria = pytz.timezone('America/Argentina/Buenos_Aires')

            # Obtener la fecha y hora actual en la zona horaria especificada
            fecha_hora_actual = datetime.datetime.now(zona_horaria)

            # Obtener la fecha en formato dd/mm/aa
            fecha_actual = fecha_hora_actual.strftime("%d/%m/%y")

            # Obtener la hora en formato hh:mm:ss
            hora_actual = fecha_hora_actual.strftime("%H:%M:%S")

            # Escribimos la fecha actual 
            c.setFont("Helvetica", 10)
            c.drawString(40, 760, f"{fecha_actual} - {hora_actual}")

            # Agregar título
            c.setFont("Helvetica-Bold", 32)
            titulo = "Calculadora Cuota Simple"
            titulo_width = c.stringWidth(titulo, "Helvetica-Bold", 32)
            titulo_x = (letter[0] - titulo_width) / 2  # Centrar el título horizontalmente
            c.drawString(titulo_x, 720, titulo)

            # Coordenadas y dimensiones de la imagen
            imagen_path = "imgs/logos_came_con_fondo y recortados.png" # Reemplaza 'tu_imagen.png' con la ruta de tu propia imagen
            imagen_width = 300  # Ancho de la imagen
            imagen_height = 50  # Altura de la imagen
            imagen_x = (letter[0] - imagen_width) / 2  # Centrar la imagen horizontalmente
            imagen_y = 660  # Espacio entre el título y la imagen

            c.drawImage(imagen_path, imagen_x, imagen_y, width=imagen_width, height=imagen_height)

            # Coordenadas y dimensiones del rectángulo
            rect_width = 400  # Ancho del rectángulo
            rect_height = 50  # Altura del rectángulo
            rect_x = (letter[0] - rect_width) / 2  # Centrar el rectángulo horizontalmente
            rect_y = 580 # Espacio entre la imagen y el rectángulo

            c.rect(rect_x, rect_y, rect_width, rect_height)

            # Texto que quieres agregar dentro del rectángulo
            c.setFont("Helvetica-Bold", 20)
            texto = f"Precio sugerido: ${lista_variables[1]}"

            # Alinear el texto en el centro del rectángulo
            text_width = c.stringWidth(texto, "Helvetica-Bold", 20)
            text_x = rect_x + (rect_width - text_width) / 2
            text_y = rect_y + (rect_height - 20) / 2  # Alinear verticalmente en el centro

            # Agregar texto dentro del rectángulo
            c.drawString(text_x, text_y, texto)

            # ACLARACIÓN 
            c.setFont("Helvetica-Bold", 10)
            c.drawString(90, 555, "ACLARACIÓN")
            c.setFont("Helvetica", 9)
            c.drawString(90, 545, "El usuario reconoce y acepta que los datos generados son a título meramente informativo y orientativo.") 
            c.drawString(90, 535, "La herramienta no apunta a establecer precios finales para ninguna operación sino brindar, de manera detallada,")
            c.drawString(90, 525, "la información que un comercio puede necesitar para definir, por decisión propia,") 
            c.drawString(90, 515, "los precios de los productos y servicios que comercializa a través de las promociones del programa Cuota Simple.")
            c.drawString(90, 505, "Asimismo, CAME no se responsabiliza por la información brindada por el sistema, su actualización o su falta de disponibilidad.")  

            # Agrega una línea separadora
            line_x1, line_y1 = 100, 210
            line_x2, line_y2 = 520, 210
            # linea
            c.line(line_x1, line_y1, line_x2, line_y2)

            # TABLA 1
            x1, y1 = 90, 470  # Esquina superior izquierda
            x2, y2 = 400, 230  # Esquina inferior derecha

            # Dibuja el cuadrado
            c.rect(x1, y1, x2 - x1, y2 - y1)

            # Establece la fuente y agrega tus cadenas de texto
            c.setFont("Helvetica", 12)
            # Coordenada x para las categorías
            category_x = x1 + 10
            # Coordenada x para los valores (contra el margen derecho)
            value_x = x2 - 10
            # Espaciado vertical entre las líneas
            line_spacing = 20
            if tasas_a_STR == "19,759999999999998":
                    tasas_a_STR = "19,76"    
            c.setFont("Helvetica-Bold", 14)
            c.drawString(90, 480, "Liquidación de pago")   
            # Agrega las categorías y valores
            c.setFont("Helvetica", 12)  
            categories = [
                "Venta a precio de contado:",
                f"Financiado en {st.session_state.programa_seleccionado}:",
                "AFIP:",
                "Arancel 1,8%:",
                f"Costo Financiero del programa ({tasas_a_STR}%):",
                "IVA Arancel (21%):",
                "IVA Costo Financiero (10,50%):",
                "Subtotal",
                "IVA RG 140/98 (3%)",
                "Total Cobrado en la liquidación"  
            ]

            values = [
                f"${lista_variables[0]}",
                f"${lista_variables[1]}",
                st.session_state.tipo_inscripcion,
                f"${lista_variables[2]}",
                f"${lista_variables[3]}",
                f"${lista_variables[4]}",
                f"${lista_variables[5]}",
                f"${lista_variables[6]}",
                f"${lista_variables[7]}",
                f"${lista_variables[8]}"    
            ]

            # Índices de los valores que deseas en negrita
            bold_indices = [8,10]

            for i in range(len(categories)):
                category = categories[i]
                value = values[i]

                # Utiliza la fuente en negrita para los valores específicos
                if i in bold_indices:
                    c.setFont("Helvetica-Bold", 12)
                else:
                    c.setFont("Helvetica", 12)

                # Dibuja la categoría y el valor
                c.drawString(category_x, 450 - i * line_spacing, category)
                c.drawString(value_x - c.stringWidth(value, "Helvetica-Bold" if i in bold_indices else "Helvetica", 12), 450 - i * line_spacing, value)

            # TABLA 2


                # TABLA 1
            x1, y1 = 90, 180  # Esquina superior izquierda
            x2, y2 = 400, 10  # Esquina inferior derecha

            # Dibuja el cuadrado
            c.rect(x1, y1, x2 - x1, y2 - y1)

            # Establece la fuente y agrega tus cadenas de texto
            c.setFont("Helvetica", 12)
            # Coordenada x para las categorías
            category_x = x1 + 10
            # Coordenada x para los valores (contra el margen derecho)
            value_x = x2 - 10
            # Espaciado vertical entre las líneas
            line_spacing = 20
                
            c.setFont("Helvetica-Bold", 14)
            c.drawString(90, 190, f"Cálculo de impuestos")
            # Agrega las categorías y valores
            c.setFont("Helvetica", 12)    
            categories = [
                "Venta neta IVA",
                "IVA Débito",
                "IVA Crédito",
                "Posición IVA",
                "Saldo cobrado",
                "Tasa Municipal (1%)",
                "IIBB",
                "Utilidad Antes de Costos e IIGG"  
            ]

            values = [
                f"${lista_variables[9]}",
                f"${lista_variables[10]}",
                f"${lista_variables[11]}",
                f"${lista_variables[12]}",
                f"${lista_variables[13]}",
                f"${lista_variables[14]}",
                f"${lista_variables[15]}", 
                f"${lista_variables[16]}"    
            ]

            # Índices de los valores que deseas en negrita
            bold_indices = [3,7]

            for i in range(len(categories)):
                category = categories[i]
                value = values[i]

                # Utiliza la fuente en negrita para los valores específicos
                if i in bold_indices:
                    c.setFont("Helvetica-Bold", 12)
                else:
                    c.setFont("Helvetica", 12)

                # Dibuja la categoría y el valor
                c.drawString(category_x, 160 - i * line_spacing, category)
                c.drawString(value_x - c.stringWidth(value, "Helvetica-Bold" if i in bold_indices else "Helvetica", 12), 160 - i * line_spacing, value)
                


            # Guardar y cerrar el PDF
            c.save()
            pdf_buffer.seek(0)
            

            aux = True

            custom_css2 = """
                    <style>
                        body {
                            font-family: 'Arial', sans-serif;
                        }
                        .card {
                            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.6), 0 4px 8px rgba(0, 0, 0, 0.3);
                            border-radius: 10px;
                            padding: 10px; /* Ajusta el espacio interno superior e inferior */
                            margin-bottom: 20px;
                            margin-right: 10px; /* Ajusta el espacio en el lado derecho */
                            background: #005CA7;
                            color: #ecf0f1;
                            border: 2px solid #ffffff;
                            text-align: center; /* Centra el texto horizontalmente */
                            display: flex;
                            flex-direction: column;
                            align-items: center;
                            justify-content: center;
                            height: 150px; /* Ajusta la altura de la tarjeta según sea necesario */
                        }
                        .card h2 {
                            font-size: 1.5em;
                            color: #ffffff;
                        }
                        .card p {
                            font-size: 2.9em;
                        }
                    </style>
                """

            st.markdown(custom_css2, unsafe_allow_html=True)

            # TARJETA PRECIO SUGERIDO
            st.markdown(f'<div class="card"><h2 style="color: #ffffff;">El precio sugerido a cobrar es:</h2><p>${lista_variables[1]}</p></div>', unsafe_allow_html=True)

            # FORMULARIO DE CALIFICACIÓN
            with st.form(key='calificacion usuario'):
                # Evaluación       
                evaluation = st.radio("¿Cómo calificaría el funcionamiento de la calculadora?", ["Excelente", "Buena", "Regular", "Mala", "Muy mala"],horizontal=True)
                # Botón de calificación
                submit_button = st.form_submit_button(label='Enviar')
                # Verificar si el formulario se ha enviado
                if submit_button:
                    # Agregar st.write para verificar el valor de evaluation
                    try:
                        calificacion(fecha_actual, hora_actual, evaluation)
                        st.success("Calificación enviada exitosamente!")
                    # Si salta error, esperar dos segundos y volver a cargar    
                    except github.GithubException:
                        try:
                            time.sleep(2)
                            calificacion(fecha_actual, hora_actual, evaluation)
                            st.success("Calificación enviada exitosamente!")
                        except github.GithubException:
                            pass
                    
                
              
            if aux == True : 
                st.write("---")
                st.write(f"+ ##### Precio de contado: ${lista_variables[0]}")
                st.write(f"+ ##### Precio sugerido a cobrar: ${lista_variables[1]}")
                st.write(f"+ ##### Total de descuentos en pesos: ${lista_variables[17]}")
                st.write("**ACLARACIÓN**: Los montos se calcularon en base al precio sugerido, aplicando los descuentos correspondientes al programa seleccionado, IVA, IIBB y la tasa municipal.")
                
            if aux == True : 
                st.write("---")
                st.write("**Detalle de descuentos:**")
                if tasas_a_STR == "19,759999999999998":
                    tasas_a_STR = "19,76"
                st.write(f"+ Tasa del programa {programa_seleccionado} ({tasas_a_STR}%): **${lista_variables[3]}**")
                st.write(f"+ Arancel T.Cred (1,8%): **${lista_variables[2]}**")
                st.write(f"+ IVA (21%): **${lista_variables[4]}**")
                st.write(f"+ IVA (10,5%) ley 25.063: **${lista_variables[5]}**")
                st.write(f"###### **Subtotal: ${lista_variables[6]}**")   
                st.write(f"+ IVA RG 140/98 (3%): **${lista_variables[7]}**") 
                st.write(f"+ **Liquidación: ${lista_variables[8]}**") 
                st.write("---")
                st.write(f"+ Venta neta de IVA: **${lista_variables[9]}**")     
                st.write(f"+ IVA Débito (sobre venta neta): **${lista_variables[10]}**")     
                st.write(f"+ IVA Crédito (sobre costo financieros): **${lista_variables[11]}**") 
                st.write(f"###### **Posición IVA: ${lista_variables[12]}**")   
                st.write(f"+ Tasa Municipal (1%): **${lista_variables[14]}**")     
                st.write(f"+ II.BB (Alícuota Gral: {alicuota_a_STR}%): **${lista_variables[15]}**")
                #st.write(f"##### **Utilidad Antes de Costos e IIGG**: ${lista_variables[16]}")
                    
            st.write("---") 
            #COLOCAMOS EL BOTON DE DESCARGA AL FINAL
            col4, col5, col6 = st.columns([1,2,1])
            with col4:
                st.write("")
            with col5:
                # Botón de descarga
                st.download_button("Descargar PDF", pdf_buffer, file_name="Resumen precio sugerido.pdf",use_container_width=True)
            with col6:
                st.write("")
                
            enlace_externo = "https://forms.gle/4Q4cq3XLPRdnX6q27"
            # Definir el código HTML y CSS para el botón personalizado
            boton_html = f"""
                <style>
                    .enlace-btn {{
                        background-color: white; /* Color de fondo */
                        color: #005CA7; /* Color del texto */
                        padding: 10px 20px; /* Espaciado interno */
                        text-align: center; /* Alineación del texto */
                        text-decoration: none; /* Sin subrayado */
                        display: inline-block;
                        font-size: 16px; /* Tamaño del texto */
                        cursor: pointer; /* Tipo de cursor */
                        border-radius: 5px; /* Bordes redondeados */
                        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Sombra */
                        border: 2px solid #005CA7; /* Delineado azul */
                    }}
                    .enlace-btn:hover {{
                        color: #005CA7; /* Cambiar color del texto al pasar el ratón */
                    }}
                </style>
                <a class="enlace-btn" href="{enlace_externo}" target="_blank">Responder encuesta del programa</a>
            """
            # Mostrar el botón personalizado
            st.markdown(boton_html, unsafe_allow_html=True)
            st.write("**Aclaración**")
            st.write("Por cuestiones metodológicas, el cálculo se basa en ingresos brutos por el 3,5% y Tasa municipal por 1%")
            st.write("El usuario reconoce y acepta que los datos generados son a título meramente informativo y orientativo. La herramienta no apunta a establecer precios finales para ninguna operación sino brindar, de manera detallada, la información que un comercio puede necesitar para definir, por decisión propia, los precios de los productos y servicios que comercializa a través de las promociones del programa Cuota Simple. Asimismo, CAME no se responsabiliza por la información brindada por el sistema, su actualización o su falta de disponibilidad.")
            st.markdown("Para mayor información [click aquí](https://www.argentina.gob.ar/economia/comercio/cuota-simple)")
            st.write("---")

            if aux == True and st.session_state.carga_inicial == False:
                try:
                    calculo(fecha_actual, hora_actual, lista_variables[0], lista_variables[1], st.session_state.programa_seleccionado, tipo_inscripcion, st.session_state.provincia_seleccionada)
                    st.session_state.carga_inicial = True
                # Si salta error, esperar dos segundos y volver a cargar    
                except github.GithubException:
                    try:
                        time.sleep(3)
                        calculo(fecha_actual, hora_actual, lista_variables[0], lista_variables[1], st.session_state.programa_seleccionado, tipo_inscripcion, st.session_state.provincia_seleccionada)
                        st.session_state.carga_inicial = True
                    except github.GithubException:
                        pass       

if st.checkbox("Si usted tiene alguna consulta, haga click aquí"):
    with st.form(key='consultas'):
        st.write("Si tiene alguna consulta, por favor complete los siguientes campos.")
        nombre, apellido, asunto = st.columns(3)
        with nombre:
            nombre_ingresado = st.text_input("Nombre")
        with apellido:    
            apellido_ingresado = st.text_input("Apellido")
        with asunto:
            asunto_ingresado = st.text_input("Asunto")

        email, repetir_email = st.columns(2)
        with email:
            email_ingresado = st.text_input("Ingrese su e-mail")
        with repetir_email:
            repetir_email_ingresado = st.text_input("Ingrese su e-mail nuevamente")
            
        # Consulta
        consulta_ingresada = st.text_area("Escriba su consulta aquí", key='consulta_text_area') 

        # Botón de consulta
        boton_consulta = st.form_submit_button(label='Enviar')

        if boton_consulta:
            if email_ingresado.strip() != repetir_email_ingresado.strip():
                st.error("Los correos electrónicos no coinciden. Por favor, ingréselos nuevamente.")
            elif nombre_ingresado == "" or apellido_ingresado == "" or asunto_ingresado == "" or consulta_ingresada == "":
                st.error("Complete los campos necesarios por favor.")
            else:
                # aca cargar la data
                # Do something with the form data
                # Establecer la zona horaria a Buenos Aires
                zona_horaria = pytz.timezone('America/Argentina/Buenos_Aires')

                # Obtener la fecha y hora actual en la zona horaria especificada
                fecha_hora_actual = datetime.datetime.now(zona_horaria)

                # Obtener la fecha en formato dd/mm/aa
                fecha_actual = fecha_hora_actual.strftime("%d/%m/%y")

                # Obtener la hora en formato hh:mm:ss
                hora_actual = fecha_hora_actual.strftime("%H:%M:%S")        
                try:
                    consulta(fecha_actual, hora_actual, nombre_ingresado, apellido_ingresado, email_ingresado, repetir_email_ingresado ,asunto_ingresado, consulta_ingresada)
                    st.success("Consulta enviada exitosamente!") 
                # Si salta error, esperar dos segundos y volver a cargar    
                except github.GithubException:
                    try:
                        time.sleep(2)
                        consulta(fecha_actual, hora_actual, nombre_ingresado, apellido_ingresado, email_ingresado, repetir_email_ingresado ,asunto_ingresado, consulta_ingresada)
                        st.success("Consulta enviada exitosamente!") 
                    except github.GithubException:
                        pass
                

st.write("---")
# Titulo para las redes con estilo personalizado
st.markdown(
    """
    <div style="text-align: center; padding: 20px 0; margin-top: 0;">
        <h1 style="border: 2px solid #004AAD; padding: 10px; font-size: 24px; border-radius: 10px; display: inline-block;">
            ¡Seguí a CAME en redes sociales!
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Columnas para centrar
col_izq, col_centro, colder = st.columns([0.7,1.8,0.5])
with col_izq :
    st.write("")

with col_centro:
    colFc, colIg, colTw, colLk, colYt = st.columns(5)
    with colFc:
        # URL de tu perfil de Instagram
        facebook_url = "https://www.facebook.com/redcame"
        # Cargar la imagen del logotipo de Instagram
        logo_image = "imgs/facebook.png"  # Reemplaza con la ruta de tu imagen
        # Mostrar el logotipo de Instagram
        st.image(logo_image, width=32)
        # Crear un enlace clickeable
        st.markdown(f"[Facebook]({facebook_url})", unsafe_allow_html=True)

    with colIg:
        # URL de tu perfil de Instagram
        instagram_url = "https://www.instagram.com/redcame/"
        # Cargar la imagen del logotipo de Instagram
        logo_image = "imgs/ig.png"  # Reemplaza con la ruta de tu imagen
        # Mostrar el logotipo de Instagram
        st.image(logo_image, width=32)
        # Crear un enlace clickeable
        st.markdown(f"[Instagram]({instagram_url})", unsafe_allow_html=True)

    with colTw:
        # URL de tu perfil de Instagram
        twiter_url = "https://twitter.com/redcame"
        # Cargar la imagen del logotipo de Instagram
        logo_image = "imgs/twiter.png"  # Reemplaza con la ruta de tu imagen
        # Mostrar el logotipo de Instagram
        st.image(logo_image, width=32)
        # Crear un enlace clickeable
        st.markdown(f"[Twitter]({twiter_url})", unsafe_allow_html=True)

    with colLk:
        # URL de tu perfil de Instagram
        linkedin_url = "https://ar.linkedin.com/company/redcame"
        # Cargar la imagen del logotipo de Instagram
        logo_image = "imgs/linkedin.png"  # Reemplaza con la ruta de tu imagen
        # Mostrar el logotipo de Instagram
        st.image(logo_image, width=32)
        # Crear un enlace clickeable
        st.markdown(f"[LinkedIn]({linkedin_url})", unsafe_allow_html=True) 

    with colYt:
        # URL de tu perfil de Instagram
        youtube_url = "https://www.youtube.com/c/CAMEar"
        # Cargar la imagen del logotipo de Instagram
        logo_image = "imgs/yutu.png"  # Reemplaza con la ruta de tu imagen
        # Mostrar el logotipo de Instagram
        st.image(logo_image, width = 40)
        # Crear un enlace clickeable
        st.markdown(f"[Youtube]({youtube_url})", unsafe_allow_html=True)               

with colder :
    st.write("")


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
