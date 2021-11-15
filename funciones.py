def suma(numero1, numero2):
    """ Suma de dos variables.
    param int numero1 cualquier entero 
    param int numero2 cualquier entero 
    returns la sumatorioa de ambas varialbes 
    """
    total = numero1 + numero2
    return total

def suma2(numeros):
     """ Suma de todos los numeros en un arreglo .
    param Array numeros lista de enteros a sumar  
    returns la sumatorioa de todos los numeros del arreglo 
    """
     total = 0  
     for num in numeros :
        total = total + int(num)

     return total 

print(suma( 2,5 ))

arreglo = {1,4,6,8,3,5,4}
print(suma2 (arreglo))

def imprimirDato (*nombre):
    print('El nombre prompleto es: ', nombre)
    print('El nombre prompleto es: ', nombre[2])

imprimirDato('prueba', 'prueba2', 'jose', 'alberto')

def nombreCompleto(apellido, nombre):
    print(nombre,apellido)

nombreCompleto(nombre='Jose',apellido='Arosemena')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

nombreCompleto2(nombre='Josejair', apellido='Arosemena')


def miFuncion2(argumento= 'Chanchito'):
    print(argumento)

miFuncion2()
miFuncion2('JJ')

def funcionLista(lista):
    i=''
    for e in lista:
        print(e)
        i = i + e + ' '
    return i

funcionLista(['jose','jair','arosemena','juarez'])

nombres = funcionLista(['jose','jair','arosemena','juarez'])
print(nombres)

def recursion(i):
    if (i<1):
        return i 
    print(i)
    recursion(i-1)

recursion (6)

