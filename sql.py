import sqlite3 as sql

def crear_conexion_db():
    #Brief crea la conexion con la base de datos
    #Parameters no tiene
    #Return no tiene
    try:
        conexion = sql.connect("jugador.db")
        conexion.commit()
        conexion.close()
        print("Conexion exitosa")
    except:
        print("No se ha podido crear la conexion con la base de datos")

def crear_tabla():
    try:
        conexion = sql.connect("jugador.db")
        cursor = conexion.cursor()
        cursor.execute(
            '''CREATE TABLE jugador  (
                nombre text,
                puntaje integer
            )'''
            )
        conexion.commit()
        conexion.close()
    except:
        print("Error al intentar crear la tabla")

def insertar_jugador(nombre, puntaje):
    conexion = sql.connect("jugador.db")
    cursor = conexion.cursor()
    nombre = nombre.title()
    instruccion = f"INSERT INTO jugador VALUES('{nombre}',{puntaje})"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()

def leer_puntajes():
    conexion = sql.connect("jugador.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM jugador"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print(datos)

def leer_items_ordenados(criterio):
    conexion = sql.connect("jugador.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM jugador ORDER BY {criterio} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()

    print(datos)

def buscar_puntajes_altos():
    conexion = sql.connect("jugador.db")
    cursor = conexion.cursor()
    instruccion = "SELECT * FROM jugador WHERE puntaje > 15 ORDER BY puntaje DESC LIMIT 3"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return datos

def actualizar_datos(puntaje, nombre):
    conexion = sql.connect("jugador.db")
    cursor = conexion.cursor()
    instruccion = f"UPDATE jugador SET puntaje = {puntaje} WHERE name like '{nombre}' "
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()


