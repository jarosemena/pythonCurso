def esMayor(usuario):
    return usuario.edad > 17 

class Usuarios:
    def __init__(self, edad):
        self.edad = edad 

usuario1 = Usuarios(15)
usuario2 = Usuarios(21)

print(esMayor(usuario1),esMayor(usuario2))
