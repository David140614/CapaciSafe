import psycopg2

# Configuración de la base de datos en Railway
config = {
    "host": "shortline.proxy.rlwy.net",
    "user": "postgres",
    "password": "LVrPkwetUOVhadeiAdRCvsFcQxXYlpwo",
    "database": "railway",
    "port": 34451
}

try:
    # Conectar a la base de datos
    connection = psycopg2.connect(**config)
    print(" Conexión exitosa a PostgreSQL en Railway")

    # Crear un cursor y ejecutar una consulta de prueba
    cursor = connection.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tables = cursor.fetchall()
    print(" Tablas en la base de datos:", tables)

except psycopg2.Error as err:
    print(f" Error: {err}")

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print(" Conexión cerrada")
