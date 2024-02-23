Módulo de OCR para el PAC
Este módulo de OCR (Reconocimiento Óptico de Caracteres) está diseñado para procesar archivos PDF y extraer información relevante utilizando FastAPI. El objetivo principal es proporcionar una solución rápida y eficiente para la extracción de datos de documentos en formato PDF.

Características


Endpoint read_pdf: Este módulo presenta un endpoint llamado read_pdf, al cual se puede subir un archivo PDF para que el sistema extraiga los datos y devuelva un objeto JSON con la información obtenida.


Integración con FastAPI: FastAPI se utiliza como el marco web para la creación del servidor web que maneja las solicitudes HTTP y la lógica de negocio relacionada con el OCR.


Ejecución con Docker: El módulo de OCR se ejecuta dentro de un contenedor Docker para facilitar la portabilidad y la gestión de dependencias.



Uso

Requisitos Previos
Asegúrate de tener Docker instalado en tu sistema antes de ejecutar este módulo. Si no tienes Docker instalado, puedes encontrar instrucciones de instalación en el sitio web oficial de Docker.

Ejecución


Clona este repositorio en tu máquina local:
git clone https://gitlab.emergiacc.com/dflunan/ocr-pac.git


Navega al directorio del repositorio clonado:
cd ocr-pac


Construye la imagen Docker:
docker build -t ocr-pac .


Ejecuta el contenedor Docker:
docker run -p 8000:8000 ocr-pac


El servidor FastAPI estará ahora en funcionamiento y listo para procesar solicitudes en el puerto 8000.

Acceso a la Documentación
Una vez que el servidor esté en funcionamiento, puedes acceder a la documentación generada automáticamente por FastAPI visitando localhost:8000/docs/. Esta documentación proporciona información detallada sobre todos los endpoints disponibles, así como la forma de interactuar con ellos.

Uso del Endpoint read_pdf

Una vez que el servidor esté en funcionamiento, puedes enviar solicitudes al endpoint read_pdf para extraer datos de un archivo PDF. Aquí tienes un ejemplo de cómo hacerlo utilizando cURL:
curl -X POST -F "file=@ruta/al/archivo.pdf" http://localhost:8000/read_pdf
Sustituye ruta/al/archivo.pdf con la ruta completa de tu archivo PDF.
El servidor responderá con un objeto JSON que contiene los datos extraídos del PDF.