lista = []
print('Ingrese los numeros que desea sumar y cuanto terminte escriba "stop"')
while True:
    valor = input('Ingrese un valor: ')
    if valor == 'stop':
        break
    else:
        try:
            valor = float(valor)
            lista.append(valor)
        except:
            print("El valor ingresado no es valido")

resultado = 0 
for item in lista:
    resultado += item

print(resultado)