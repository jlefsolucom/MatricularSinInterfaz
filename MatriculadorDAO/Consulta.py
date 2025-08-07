from DataBase.BD import conectar

def obtener_datos():
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM vw_consulta_crea_RFID")
        resultados = [fila for fila in cursor.fetchall()]
        conexion.close()
        return resultados
    return []


def insertar_datos_huella(Cod_Padron, desc_codigo, imgn_raw):
    num_validez = 0
    ind_estado = "A"
    ind_notif = 1
    ind_tipo_LLave = 5

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        qwery = """ INSERT INTO mnt_codigo_persona
        (Cod_Padron, Desc_Codigo, Num_Validez, ind_estado, ind_notif, ind_tipo_LLave, img)
        values(%s,%s,%s,%s,%s,%s,%s)"""
        valores = (Cod_Padron, desc_codigo, num_validez, ind_estado,
                   ind_notif, ind_tipo_LLave, imgn_raw)

        cursor.execute(qwery, valores)
        conexion.commit()
        conexion.close()


def insertar_tarjeta(codigo_bash, desc_codigo, Cod_Padron):
    num_validez = 0
    ind_estado = "A"
    ind_notif = 1
    ind_tipo_LLave = 2

    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()

        print(Cod_Padron)
        qwery = """ INSERT INTO mnt_codigo_persona
        (Cod_Padron, Val_Codigo, Desc_Codigo, Num_Validez, ind_estado, ind_notif, ind_tipo_LLave)
        values(%s,%s,%s,%s,%s,%s,%s)"""
        valores = (Cod_Padron, codigo_bash, desc_codigo, num_validez, ind_estado,
                   ind_notif, ind_tipo_LLave)
        try:
            cursor.execute(qwery, valores)
            conexion.commit()
            print("Insertado")
        except Exception as e:
            print("Error",e)
        finally:
            conexion.close()