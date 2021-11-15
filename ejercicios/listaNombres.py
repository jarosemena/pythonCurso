def agregar(nombre,apellido):
    file = open('listaNombres.txt','a')
    
    file.write(nombre + ' ' + apellido +'\n')

    file.close()


agregar('Jose','Arosemena')
agregar('Jair','Juarez')
agregar('Jose','Juarez')
agregar('Jair','Arosemena')
agregar('Jose jair','Arosemena')

file = open('listaNombres.txt','r')
print(file.read())
file.close()