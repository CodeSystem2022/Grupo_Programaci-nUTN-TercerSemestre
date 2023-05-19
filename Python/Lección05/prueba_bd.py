import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd'
)
try:  
    with conexion: 
        with conexion.cursor() as cursor:
            sentencia = 'SELECT id_persona nombre FROM persona'
            cursor.execute(sentencia) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall() # Recuperamos todos los registros que serán una lista
            print(registros)
except Exception as e:
    print(f'Ocurrio un error:{e}')
finally:
    conexion.close()