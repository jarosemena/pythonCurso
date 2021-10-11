class Animal:
    def __init__(self,nombre,onomatopeya,sistema='Digestivo'):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
        self.sistemaDigestivo=sistema
       
        
    def saludo(self):
        print ('Hola soy un ', self.tipo,', mi nombre es ', self.nombre,' y mi sonido es',self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self,nombre,onomatopeya):
        Animal.__init__(self,nombre, onomatopeya)
        

class Perro(Animal):
    tipo= 'perro'
    def __init__(nombre, onomatopeya):
        super().__init__(nombre,onomatopeya)

gato = Gato('fluffy','maullido')
gato.saludo()

perro = Perro('firulay','ladrido')
perro.saludo()

