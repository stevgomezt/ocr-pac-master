import mysql.connector
import json
import requests
from flask import Flask, render_template, request, redirect, url_for

# Establecer conexión a la base de datos MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="flask_login"
)

# Crear un cursor para ejecutar consultas
cursor = db_connection.cursor()

app = Flask(__name__)

# URL de Docker donde se debe enviar la solicitud
DOCKER_URL = 'http://localhost:8000/ocr/api/v1/read_pdf/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        # Obtener los datos adicionales del formulario
        additionalData1 = request.form['additionalData1']
        additionalData2 = request.form['additionalData2']

        # Definir los encabezados
        headers = {
            'accept': 'application/json',
        }

        # Definir los datos del formulario
        files = {
            'file': (file.filename, file.stream, 'application/pdf')
        }

        # Realizar la solicitud POST a la URL de Docker
        response = requests.post(DOCKER_URL, headers=headers, files=files)

        # Guardar la respuesta en la base de datos MySQL
        if response.status_code == 200:
            # Obtener el JSON de la respuesta
            json_data = response.json()

            # Extraer el primer elemento del JSON (la respuesta es una lista con un solo diccionario)
            data = json_data[0] if json_data else {}

            # Definir una función auxiliar para obtener el valor de un campo o devolver None si no está presente
            def get_field(field_name):
                return data.get(field_name)

            # Insertar los datos en la tabla MySQL
            insert_query = """
                INSERT INTO datos_evaluacion 
                (Energia_Adaptado,
                Energia_Natural,
                Equilibrio_de_Energia,
                Intensidad_Perfil_Adaptado,
                Intensidad_Perfil_Natural,
                Modificacion_perfil,
                Nombre_Asesor,
                Perfil_Adaptado_A,
                Perfil_Adaptado_A_num,
                Perfil_Adaptado_A_IE,
                Perfil_Adaptado_E,
                Perfil_Adaptado_E_num,
                Perfil_Adaptado_E_IE,
                Perfil_Adaptado_N,
                Perfil_Adaptado_N_num,
                Perfil_Adaptado_N_IE,
                Perfil_Adaptado_P,
                Perfil_Adaptado_P_num,
                Perfil_Adaptado_P_IE,
                Perfil_Adaptado_R,
                Perfil_Adaptado_R_num,
                Perfil_Adaptado_R_IE,
                Perfil_Natural_A,
                Perfil_Natural_A_num,
                Perfil_Natural_A_IE,
                Perfil_Natural_E,
                Perfil_Natural_E_num,
                Perfil_Natural_E_IE,
                Perfil_Natural_N,
                Perfil_Natural_N_num,
                Perfil_Natural_N_IE,
                Perfil_Natural_P,
                Perfil_Natural_P_num,
                Perfil_Natural_P_IE,
                Perfil_Natural_R,
                Perfil_Natural_R_num,
                Perfil_Natural_R_IE,
                Tiempo_Formulario,
                Toma_decisiones_Adaptado,
                Toma_decisiones_Natural,
                Unidad_tiempo,
                additionalData1,
                additionalData2)
                VALUES 
                (%s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s,
                %s,
                %s)
            """
            cursor.execute(insert_query, (
                get_field("Energia Adaptado"),
                get_field("Energia Natural"),
                get_field("Equilibrio de Energia"),
                get_field("Intensidad Perfil Adaptado"),
                get_field("Intensidad Perfil Natural"),
                get_field("Modificacion perfil"),
                get_field("Nombre Asesor"),
                get_field("Perfil Adaptado A"),
                get_field("Perfil Adaptado A#"),
                get_field("Perfil Adaptado A_IE"),
                get_field("Perfil Adaptado E"),
                get_field("Perfil Adaptado E#"),
                get_field("Perfil Adaptado E_IE"),
                get_field("Perfil Adaptado N"),
                get_field("Perfil Adaptado N#"),
                get_field("Perfil Adaptado N_IE"),
                get_field("Perfil Adaptado P"),
                get_field("Perfil Adaptado P#"),
                get_field("Perfil Adaptado P_IE"),
                get_field("Perfil Adaptado R"),
                get_field("Perfil Adaptado R#"),
                get_field("Perfil Adaptado R_IE"),
                get_field("Perfil Natural A"),
                get_field("Perfil Natural A#"),
                get_field("Perfil Natural A_IE"),
                get_field("Perfil Natural E"),
                get_field("Perfil Natural E#"),
                get_field("Perfil Natural E_IE"),
                get_field("Perfil Natural N"),
                get_field("Perfil Natural N#"),
                get_field("Perfil Natural N_IE"),
                get_field("Perfil Natural P"),
                get_field("Perfil Natural P#"),
                get_field("Perfil Natural P_IE"),
                get_field("Perfil Natural R"),
                get_field("Perfil Natural R#"),
                get_field("Perfil Natural R_IE"),
                get_field("Tiempo Formulario"),
                get_field("Toma decisiones Adaptado"),
                get_field("Toma decisiones Natural"),
                get_field("Unidad tiempo"),
                additionalData1,
                additionalData2)
            )
            db_connection.commit()

            message = 'Información guardada en la base de datos'
            return redirect(url_for('index', message=message))
        else:
            return 'Error al procesar el archivo: {}'.format(response.text)


if __name__ == '__main__':
    app.run(debug=True)
