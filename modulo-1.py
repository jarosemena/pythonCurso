import ModuloT as mod
from modulos import saludo, mascotas
from camelcase import CamelCase

print(mascotas)
saludo('Nicolas')

print (mod.masotas)
mod.saludo('Jose Jair')

c = CamelCase()
s = 'esta oración necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)
