import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='jair',
    password='Jojaseir29',
    database='prueba'
)

cursor = midb.cursor()


# insertar y consultar datos 
# cursor.execute('select * from Usuario')
# sql = 'insert into Usuario (email,username,edad) VALUES (%s,%s,%s)'
# values = ('j@gmail.com','jose arosemena',33)

# cursor.execute(sql,values)
# midb.commit()

# cursor.execute('select * from Usuario')


## actualizar y consultardatos 
# sql = 'update Usuario set email = %s where id = %s'
# values = ('otro@gmail.com',8)

# cursor.execute(sql,values)
# midb.commit()

# cursor.execute('select * from Usuario')

# resultado = cursor.fetchall()
#  resultado = cursor.fetchone()


## eliminar un registro de base de datos
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

# sql = 'delete from Usuario where id = %s'
# values = (10,)

# cursor.execute(sql,values)
# midb.commit()

# cursor.execute('select * from Usuario')

# resultado = cursor.fetchall()

## limitar la consulta 
sql = 'select * from Usuario limit 2'
cursor.execute(sql)

resultado = cursor.fetchall()

print(resultado)

