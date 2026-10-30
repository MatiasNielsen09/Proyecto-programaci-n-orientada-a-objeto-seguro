


import oracledb
from db import conectar


def probar_conexion():
    print("Iniciando prueba de conexión a EcoTech Solutions...")
    try:
        # El bloque 'with' asegura que la conexión se cierre automáticamente
        with conectar() as conexion:
            print("Conexión correcta a Oracle Database.")
            print(f"Versión del servidor: {conexion.version}")
            print("Entorno configurado correctamente para persistir datos.")
            
    except oracledb.Error as error:
        print(f"Error de Oracle: No se pudo conectar a la base de datos. Detalle: {error}")

if __name__ == "__main__":
    probar_conexion()