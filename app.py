from flask import Flask, render_template, request, redirect, url_for
from basedatos import insertar_asesor
import requests

app = Flask(__name__)

# URL de Docker donde se debe enviar la solicitud
DOCKER_URL = 'http://localhost:8000/ocr/api/v1/read_pdf/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guardar_asesor', methods=['POST'])
def guardar_asesor():
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

            if json_data:  # Verificar si la lista no está vacía
                # Extraer el primer elemento del JSON (la respuesta es una lista con un solo diccionario)
                data = json_data[0]

                # Insertar los datos en la tabla MySQL
                insertar_asesor(
                    data, additionalData1, additionalData2)

            message = 'Información guardada en la base de datos'
            return redirect(url_for('index', message=message))
        else:
            return 'Error al procesar el archivo: {}'.format(response.text)


if __name__ == '__main__':
    app.run(debug=True)
