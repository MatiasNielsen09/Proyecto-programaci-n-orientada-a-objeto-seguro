


import oracledb

# Reemplaza con tus credenciales asignadas por el docente
USUARIO = "POO_NIELSEN"
CLAVE = "Poo2026_55"
DSN = "54.145.68.239:1521/FREEPDB1"

def conectar():
    return oracledb.connect(
        user=USUARIO,
        password=CLAVE,
        dsn=DSN
    )