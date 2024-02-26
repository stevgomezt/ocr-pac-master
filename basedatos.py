# Importa pymysql y la extensión MySQL de Flask.
import pymysql
from flask_mysqldb import MySQL

# Inicializa el objeto MySQL para su uso con Flask.
mysql = MySQL()


def dame_conexion():
    # Esta función crea y retorna una nueva conexión a la base de datos MySQL.
    return pymysql.connect(
        host='localhost',      # Dirección del servidor de la base de datos.
        # Nombre de usuario para acceder a la base de datos.
        user='admin',
        password='admin',      # Contraseña para el usuario especificado.
        # Nombre de la base de datos a la que conectarse.
        db='flask_login'
    )


def insertar_asesor(json_data, additionalData1, additionalData2):
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Utiliza un manejador de contexto para asegurar que los recursos se liberen después de la operación.
    with conexion.cursor() as cursor:
        # Ejecuta una consulta SQL para insertar un nuevo asesor con los datos proporcionados.
        cursor.execute(
            "INSERT INTO datos_evaluacion (Energia_Adaptado,Energia_Natural,Equilibrio_de_Energia,Intensidad_Perfil_Adaptado,Intensidad_Perfil_Natural,Modificacion_perfil,Nombre_Asesor,Perfil_Adaptado_A,Perfil_Adaptado_A_num,Perfil_Adaptado_A_IE,Perfil_Adaptado_E,Perfil_Adaptado_E_num,Perfil_Adaptado_E_IE,Perfil_Adaptado_N,Perfil_Adaptado_N_num,Perfil_Adaptado_N_IE,Perfil_Adaptado_P,Perfil_Adaptado_P_num,Perfil_Adaptado_P_IE,Perfil_Adaptado_R,Perfil_Adaptado_R_num,Perfil_Adaptado_R_IE,Perfil_Natural_A,Perfil_Natural_A_num,Perfil_Natural_A_IE,Perfil_Natural_E,Perfil_Natural_E_num,Perfil_Natural_E_IE,Perfil_Natural_N,Perfil_Natural_N_num,Perfil_Natural_N_IE,Perfil_Natural_P,Perfil_Natural_P_num,Perfil_Natural_P_IE,Perfil_Natural_R,Perfil_Natural_R_num,Perfil_Natural_R_IE,Tiempo_Formulario,Toma_decisiones_Adaptado,Toma_decisiones_Natural,Unidad_tiempo,additionalData1,additionalData2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",
            # Parámetros que se pasan a la consulta SQL.
            (json_data.get("Energia Adaptado"),
             json_data.get("Energia Natural"),
             json_data.get("Equilibrio de Energia"),
             json_data.get("Intensidad Perfil Adaptado"),
             json_data.get("Intensidad Perfil Natural"),
             json_data.get("Modificacion perfil"),
             json_data.get("Nombre Asesor"),
             json_data.get("Perfil Adaptado A"),
             json_data.get("Perfil Adaptado A#"),
             json_data.get("Perfil Adaptado A_IE"),
             json_data.get("Perfil Adaptado E"),
             json_data.get("Perfil Adaptado E#"),
             json_data.get("Perfil Adaptado E_IE"),
             json_data.get("Perfil Adaptado N"),
             json_data.get("Perfil Adaptado N#"),
             json_data.get("Perfil Adaptado N_IE"),
             json_data.get("Perfil Adaptado P"),
             json_data.get("Perfil Adaptado P#"),
             json_data.get("Perfil Adaptado P_IE"),
             json_data.get("Perfil Adaptado R"),
             json_data.get("Perfil Adaptado R#"),
             json_data.get("Perfil Adaptado R_IE"),
             json_data.get("Perfil Natural A"),
             json_data.get("Perfil Natural A#"),
             json_data.get("Perfil Natural A_IE"),
             json_data.get("Perfil Natural E"),
             json_data.get("Perfil Natural E#"),
             json_data.get("Perfil Natural E_IE"),
             json_data.get("Perfil Natural N"),
             json_data.get("Perfil Natural N#"),
             json_data.get("Perfil Natural N_IE"),
             json_data.get("Perfil Natural P"),
             json_data.get("Perfil Natural P#"),
             json_data.get("Perfil Natural P_IE"),
             json_data.get("Perfil Natural R"),
             json_data.get("Perfil Natural R#"),
             json_data.get("Perfil Natural R_IE"),
             json_data.get("Tiempo Formulario"),
             json_data.get("Toma decisiones Adaptado"),
             json_data.get("Toma decisiones Natural"),
             json_data.get("Unidad tiempo"),
             additionalData1,
             additionalData2))
        # Confirma la transacción.
        conexion.commit()
        # Cierra la conexión a la base de datos.
    conexion.close()
