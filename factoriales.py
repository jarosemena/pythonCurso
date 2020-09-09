def factorial(n):
    """Calcula el factorial de un numero
       param n int cualquier entero mayor a 0 
       return n!
       """

    if n==1 :
        return 1 

    return n * factorial(n-1)

n = int(input('Escribe un numero Entero: '))

print(factorial(n))
