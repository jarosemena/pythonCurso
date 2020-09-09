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