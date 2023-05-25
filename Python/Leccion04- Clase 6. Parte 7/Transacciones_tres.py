import psycopg2 as bd # Esto es para poder conectarnos a Postgret

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor()as cursor:
            sentecia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'arojas@gmail.com')
            cursor.execute(sentecia,valores)

            sentecia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%'
            valores = ('Juan Carlos', 'Roldan', 'jcroldan@gmail.com',1)
            cursor.execute(sentecia, valores)

except Exception as e:
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()

print('Termina la transaccion')