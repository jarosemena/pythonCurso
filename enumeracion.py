objetivo = int(input('Escoge un entero: '))
count = 0 
respuesta = 0 

while respuesta**2 < objetivo:
    respuesta += 1 
    count += 1
    
if respuesta**2 == objetivo :
        print (f'La raiz cuadrada de {objetivo} es {respuesta}')
else :
        print (f'El nuemero objetivo {objetivo} no tine una raiz cuadrada exacta')   

print (f'{count} iteraciones')