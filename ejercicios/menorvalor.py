def menor(lista):
    resp = lista[0]
    for item in lista:
        if resp > item:
            resp = item
    
    return resp


print('el menor valor de la lista es: ',menor([1,2,3,4,55,-24,-13]))