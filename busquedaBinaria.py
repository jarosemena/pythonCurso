objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
bajo=0.0
alto = max(1.0, objetivo)
respuesta = (alto +bajo) /2 
count = 0 

while abs(respuesta**2 - objetivo) >= epsilon :
    count += 1
    if respuesta**2 < objetivo :
         bajo = respuesta
    else :
        alto = respuesta 

    respuesta = (alto + bajo ) / 2 

print (f'La Raiz cuadrada de {objetivo} es {respuesta} ')       
print (f'{count} iteraciones')