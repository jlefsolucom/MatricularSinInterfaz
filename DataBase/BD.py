import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="192.168.196.40",
            user="master",
            passwd="Mysql.25$",
            database="EntryCheck_V2_0",
            port="25010",
            auth_plugin="mysql_native_password"
        )
        return conexion
    except mysql.connector.Error as error:
        print(f"Error conectando {error}")
        return None