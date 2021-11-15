class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
#    nombre ='DEMO'
#    apellido='User'
    def saludo(self):
        print("hola mi nombre es: ",self.nombre, self.apellido)


class Admin(Usuario):
    def superSaludo(self):
        self.saludo() 
        print ('Soy Administrador')

usuario = Usuario('Jose','Arosemena')
usuario2 = Usuario('Jair','Juarez')

#print (usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)
usuario.saludo()
usuario2.saludo()



admin1 = Admin('JJ','Arosemena')
admin1.superSaludo()